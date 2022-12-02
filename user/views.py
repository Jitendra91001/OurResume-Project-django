from django.shortcuts import render
from .models import profile,skill,contact,resume,certificate
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'base.html')


def home(request):
    pdata=profile.objects.all()
    sdata=skill.objects.all()
    return render(request,'user/index.html',{"data":pdata,"s":sdata})

def signup(request):
     status = False
     if request.method == 'POST':
        Name=request.POST.get("name", "")
        Email=request.POST.get("email", "")
        Mobile=request.POST.get("mobile", "")
        Message=request.POST.get("msg", "")
        res=contact(name=Name, email=Email, mobile=Mobile, massage=Message)
        res.save()
        status=True
     return render(request, 'user/contect.html', {'S':status})


def cv(request):
    rdata = resume.objects.all()
    return render(request, 'user/resume.html', {"data": rdata})


def marksheet(request):
    cdata = certificate.objects.all()
    return render(request, 'user/certificate.html', {"data": cdata})
