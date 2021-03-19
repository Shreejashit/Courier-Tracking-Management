from django.shortcuts import render,redirect
from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . import models
from django.db import IntegrityError
from django.contrib import messages
# Create your views here.

def signin(request):
    alert = False
    if request.method=="POST":
        username = request.POST['fname']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,"home.html",{'alert':True})
        else:
            return render(request,"signin.html",{'alert':False})
    return render(request,"signin.html",{'alert':alert})

   
def signup(request):
    alert = False
    try:
        if request.method=="POST":
            fname = request.POST['fname']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(fname=fname,email=email,password=password)
            user.save()
            alert = "User Created"
            return redirect('login')
    except IntegrityError as e:
            print(e)
            return render(request,"signup.html",{'alert':"User Already Exist"})
    return render(request,"signup.html",{'alert':alert})

def signout(request):
    return redirect('signin')

def home(request):
    return render(request,"home.html",{})

def enterprice(request):
    return render(request,"enterprice.html",{})

class CourierBooking(ModelForm):
    class Meta:
        model = models.courier_booking
        fields  = '__all__'

def coubk(request):
    alert = False
    if request.method=='POST':
        cid = request.POST["id"]
        fname = request.POST["fname"]   
        femail = request.POST["femail"]
        fgender = request.POST["fgender"]
        fage = request.POST["fage"]
        faddress = request.POST["faddress"]
        fmobile = request.POST["fmobile"]
        tname = request.POST["tname"]
        tgender = request.POST["tgender"]
        taddress = request.POST["taddress"]
        tmobile = request.POST["tmobile"]
        cproduct = request.POST["cproduct"]
        cweight = request.POST["cweight"]
        price = request.POST["price"]
        db = models.courier_booking(CourierId=cid, From_Name=fname,From_EmailAddress=femail,
        From_Gender=fgender,From_Age=fage,From_Address=faddress,From_Mobile=fmobile,
        To_Name=tname,To_Gender=tgender,To_Address=taddress,To_Mobile=tmobile,Product_Name=cproduct,
        Weight=cweight,Price=price)
        db.save()
        return render(request,"courier_booking.html",{'db':db,'alert':"Courier Booked Successfully"})                   
    else:
        return render(request,"courier_booking.html", {'db':db,'alert':False})  
    return render(request,"courier_booking.html", {'db':db,'alert':alert})


def billing(request):
    billing_data = models.courier_booking.objects.all()
    if request.method=='POST':
        id = request.POST['id']
        messages.success(request, 'quick receipt generated.')
        billing_data = models.courier_booking.objects.get(id=id)
        return render(request,"courier_tracking.html",{'a':billing_data})
        #return redirect('coutk')
    return render(request,"billing.html",{'bd':billing_data})

def billing_table_quick_receipt(request):
    cout=models.courier_booking.objects.all()
    if request.method=='POST':
        id = request.POST['id']
        return HttpResponse(id)
    return render(request,"billing.html",{'db':db})

def coutk(request):
    return render(request,"courier_tracking.html",{})

def outfordelivery(request):
    return render(request,"ofd.html",{})

def report(request):
    return render(request,"report.html",{})         