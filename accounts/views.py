from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import userprofile
from django.http import HttpResponse
from django.utils.text import slugify


def home(request):
    return render(request,"home.html")

def signin(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        height=request.POST.get("height")
        activity_level=request.POST.get("activity_level")
        weight=request.POST.get("weight")
        fitness_goal=request.POST.get("fitness_goal")

        username=slugify(email.split("@")[0])

        if User.objects.filter(email=email).exists():
            return HttpResponse("user already exist")

        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        userprofile.objects.create(
            user=user,
            age=age,
            weight=weight,
            height=height,
            fitness_goal=fitness_goal,
            activity_level=activity_level,
            gender=gender,
        )
        return redirect("login")   
    return render(request,"signin.html")

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get("password")

        if User.objects.filter(email=email) and User.objects.filter(password=password):
            return redirect("dashboard")
        return HttpResponse("hi")

    return render(request,"login.html")

def dashboard(request):
    return render(request,"dashboard.html")
