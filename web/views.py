from django.shortcuts import render, redirect
from  .models import *

def index(request):
    data = Update.objects.all().order_by('-id')[:3]
 
    return render(request,"index.html",{'data':data})

def base(request):
    return render(request,"partials/base.html")

def gallery(request):
    image = Gallery.objects.all()
    context = {
        'image':image
    }
    return render(request,"gallery.html",context)

def updates(request):
    datas = Update.objects.all()
    context={
        'datas':datas
    }
    return render(request,"updates.html",context)

def contentpage(request,id):
    datas = Update.objects.get(id=id)
    context={
        'datas':datas
    }

    return render(request,"updates-contentpage.html",context)

def contact(request):
    return render(request,"contact.html")