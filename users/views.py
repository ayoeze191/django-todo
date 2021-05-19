from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, r"users\user.html")
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
    
        else:
            return render(request, "users\login.html", {"message":"invalid credentials"})
    return render(request, "users\login.html")


def logout_view(request):
    logout(request)
    return render(request, r"users\login.html", {
        "message":"logged out"
    })
    
    
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        confirm_password = request.POST["confirm password"]
        if password == confirm_password:
            user = User.objects.create_user(username, email, password)
            user.save()
            send_mail('account activation', 'your account has been sucessfully created','olabodeezekiel2018@yahoo.com', [ email ], fail_silently=False)
            return HttpResponseRedirect(reverse("users:login"))
            
    return render(request, r"users\register.html")


