from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def display_topics(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topics.html',d)

def display_wp(request):
    QLWO=WebPage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_wp.html',d)

def displayaccess(request):
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'displayaccess.html',d)


def insert_topic(request):
    tn=input('Enter the topic name:')
    nto=Topic.objects.get_or_create(Topic_name=tn)[0]
    nto.save()
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topics.html',d)

def insert_webpage(request):
    n=input("Enter the Webpage:")
    tn=input('Enter the topic name:')
    u=input('Enter the URl:')
    e=input('Enter the email:')
    TO=Topic.objects.get(Topic_name=tn)
    NWO=WebPage.objects.get_or_create(Topic_name=TO,name=n,url=u,Email=e)[0]
    NWO.save()
    QLWO=WebPage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_wp.html',d)

def insert_access(request):
    pk=input("Enter the pk of Webpage:")
    a=input("Enter the Author name:")
    d=input("Enter the date:")
    wo=WebPage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=wo,Author=a,date=d)[0]
    NAO.save()
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'displayaccess.html',d)



    