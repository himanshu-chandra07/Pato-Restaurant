from django.shortcuts import render
from .models import galleryy,chef,menuu,food,pics,reservation
# Create your views here.
def about(request):
    data=chef.objects.all()
    di={
        'data':data
    }
    return render(request,'about.html',di)
def blog(request):
    return render(request,'blog.html')
def blogd(request):
    return render(request,'blog-detail.html')
def contact(request):
    return render(request,'contact.html')
def gallery(request):
    data=pics.objects.filter(cat__type__contains="INTERIOR")
    data1=pics.objects.filter(cat__type__contains="FOOD")
    data2=pics.objects.filter(cat__type__contains="EVENTS")
    data3=pics.objects.all()
    data4=pics.objects.all()[:12]
    di={
        'data':data,
        'data1':data1,
        'data2':data2,
        'data3':data3,
        'data4':data4
    }
    return render(request,'gallery.html',di)
def index(request):
    data=galleryy.objects.all()
    dic={
        'data':data
    }
    return render(request,'index.html',dic)
def menu(request):
    data=menuu.objects.filter(cat__name__contains="STARTERS")
    data1=menuu.objects.filter(cat__name__contains="DRINKS")
    data2=menuu.objects.filter(cat__name__contains="MAIN")
    data3=menuu.objects.filter(cat__name__contains="DESSERT")
    di={
        'data':data,
        'data1':data1,
        'data2':data2,
        'data3':data3
    }
    return render(request,'menu.html',di)

def reserve(request):
    date=request.POST.get('date')
    time=request.POST.get('time')
    people=request.POST.get('people')
    name=request.POST.get('name')
    phone=request.POST.get('phone')
    email=request.POST.get('email')
    print(date,email,time,people,name,phone)
    if name !="":
        et=reservation.objects.create(nameq=name,phoneq=phone,date=date,email=email,time=time,people=people)

    return render(request,'reservation.html')
