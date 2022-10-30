from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request,"home.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2'] 

        myuser = User.objects.create_user(username,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"your account is sucessfully created")

        return redirect('signin')


    return render(request,"signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, pass1=pass1)
        return redirect("base")

    else:
        return render(request, 'signin.html')     


    return render(request,"signin.html")

def base(request):
    return render(request,"base.html")

def signout(request):
    return render(request,"home.html")

def multi(request):
    p = int(request.GET["p"])
    r = float(request.GET["r"])
    t = int(request.GET["t"])
    r = r/(12*100)
    t = t *12 
    emi = (p * r * pow(1 + r, t)) / (pow(1 + r,t) - 1)
    return render(request,"result.html", {"EMI": emi})