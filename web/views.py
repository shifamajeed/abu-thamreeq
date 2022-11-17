from django.shortcuts import render, redirect
from  .models import *

def index(request):
    return render(request,"index.html")

def base(request):
    return render(request,"partials/base.html")

def gallery(request):
    image = Gallery.objects.all()
    context = {
        'image':image
    }
    return render(request,"gallery.html",context)

def updates(request):
    return render(request,"updates.html")

def contentpage(request):
    return render(request,"updates-contentpage.html")

def contact(request):
    return render(request,"contact.html")