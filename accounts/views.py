from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from .models import userprofile
from django.http import HttpResponse
from django.utils.text import slugify
import secrets
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone
from accounts.calculations import daily_requirement
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,"home.html")

def signin(request):
    if request.method=='POST':
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
            gender=gender
        )
        return redirect("login")   
    return render(request,"signin.html")



def login_view(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, "login.html", {
                "error": "Email does not exist"
            })

        user = authenticate(
            request,
            username=user.username,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            return redirect('dashboard')

        else:
            return render(request, "login.html", {
                "error": "Incorrect password"
            })

    return render(request, "login.html")


@login_required
def dashboard(request):
    profile=userprofile.objects.get(user=request.user)

    result=daily_requirement(profile)

    context={
        "profile":profile,
        "bmr":result["bmr"],
        "tdee":result["tdee"],
        "calorie_target":result["calories_target"],
        "protein_target":result["protein_target"]
    }

    return render(request,"dashboard.html",context)    
        



# def verify_email(request):

#     if request.method == "POST":

#         # STEP 1: Send OTP
#         if "send_otp" in request.POST:

#             email = request.POST.get("email", "").strip().lower()

#             otp = str(secrets.randbelow(900000) + 100000)

#             send_mail(
#                 subject="Email Verification OTP",
#                 message=f"Your OTP is {otp}. It is valid for 5 minutes.",
#                 from_email=None,
#                 recipient_list=[email],
#                 fail_silently=False,
#             )

#             request.session["otp"] = otp
#             request.session["otp_email"] = email
#             request.session["otp_expiry"] = (
#                 timezone.now() + timedelta(minutes=5)
#             ).timestamp()

#             return render(request, "verify_email.html", {
#                 "otp_sent": True,
#                 "email": email
#             })

#         # STEP 2: Verify OTP
#         elif "verify_otp" in request.POST:

#             entered_otp = request.POST.get("otp", "")

#             saved_otp = request.session.get("otp")
#             expiry = request.session.get("otp_expiry")

#             if not saved_otp or not expiry:
#                 return render(request, "verify_email.html", {
#                     "error": "Please request a new OTP."
#                 })

#             if timezone.now().timestamp() > expiry:
#                 request.session.pop("otp", None)
#                 request.session.pop("otp_expiry", None)

#                 return render(request, "verify_email.html", {
#                     "error": "OTP expired. Please request a new OTP."
#                 })

#             if secrets.compare_digest(entered_otp, saved_otp):

#                 email = request.session.get("otp_email")

#                 request.session["verified_email"] = email

#                 request.session.pop("otp", None)
#                 request.session.pop("otp_expiry", None)

#                 return render(request, "verify_email.html", {
#                     "success": "Email verified successfully!"
#                 })

#             return render(request, "verify_email.html", {
#                 "otp_sent": True,
#                 "email": request.session.get("otp_email"),
#                 "error": "Incorrect OTP. Please try again."
#             })

#     return render(request, "verify_email.html")





   
