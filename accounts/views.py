from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import userprofile


def home(request):
    return render(request,"home.html")

def signin(request):
    if request.method=='POST':
        userame=request.post.get("username")
        email=request.post.get("email")
        password=request.post.get("password")
        age=request.post.get("age")
        gender=request.post.get("gender")
        height=request.post.get("weight")
        activity_level=request.post.get("activity_level")
        weight=request.post.get("weight")
        fitness_goal=request.post.get("fittness_goal")

        user=User.objects.create_superuser(
            username=userame,
            email=email,
            password=password,
        )

        if User.objects.filter(userame=userame).exists:
            return render(request,"signup.html",{'error:username already exist'})

        if User.objects.filter(email=email).exists:
                    return render(request,"signup.html",{'error:email already exist'})

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
    return render(request,"login.html")
