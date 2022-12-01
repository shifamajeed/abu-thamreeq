from django.shortcuts import render, redirect
from  .models import *
from django.contrib import messages


def index(request):
    data = Update.objects.all().order_by('-id')[:3]
    project = Projects.objects.all()
    if request.method == "POST":
        name=request.POST['Name']
        place=request.POST['place']
        phone=request.POST['phone']
        purpose=request.POST['purpose']
        date=request.POST['date']
        time=request.POST['time']
        
        contact=Contact(name=name,place=place,phone=phone,purpose=purpose,appointmentdat=date,appointmenttime=time)
        messages.success(request, 'success')
        contact.save()
        
    context = {
        'data':data,
        'project':project
    }


    return render(request,"index.html",context)

def base(request):
    return render(request,"partials/base.html")

def gallery(request):
    image = Gallery.objects.all()
    context = {
        'image':image
    }
    return render(request,"gallery.html",context)
    
def content(request,id):
    image = Gallery.objects.get(id=id)
    context = {
        'image':image
    }
    return render(request,"gallery-contentpage.html",context)

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
    if request.method == "POST":
        name=request.POST['Name']
        place=request.POST['place']
        phone=request.POST['phone']
        purpose=request.POST['purpose']
        date=request.POST['date']
        time=request.POST['time']
        
        contact=Contact(name=name,place=place,phone=phone,purpose=purpose,appointmentdat=date,appointmenttime=time)
        messages.success(request, 'success')
        contact.save()

    return render(request,"contact.html")

