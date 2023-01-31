from django.shortcuts import render
from .models import  Student

# Create your views here.
def index(request):
    return render(request,'form1.html')
def home(request):
    data=Student.objects.all()
    return render(request,'display.html',{'std':data})

def menu(request):
    return render(request,'taskbar.html')
def first(request):
    nme=request.POST['n1']
    mail = request.POST['n2']
    rn = request.POST['n3']
    pn = request.POST['n4']
    ads = request.POST['n5']
    data=Student(Name=nme,Email=mail,Roll_no=rn,Phone_no=pn,Address=ads)
    data.save()
    return render(request,'form1.html')
def search(request):
    return render(request,'search.html')
def searchdata(request):
    s=request.POST['sr']
    data=Student.objects.filter(Name=s)
    return render(request,'display.html',{'std':data})