from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import SignupForm, LoginForm
from .models import UserDetail

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World")

def signup(request):
    if request.method == "POST":
        try:
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({
                    "success": True,
                    "message": "Signup successful!"
                }, status=201)
            else:
                return JsonResponse({
                    "error": "Form validation failed",
                    "errors": form.errors
                }, status=400)
        except Exception as e:
            print("Signup Error:", str(e))
            return JsonResponse({
                "error": "Server error occurred",
                "details": str(e)
            }, status=500)
    else:
        form = SignupForm()
    return render(request, "Loginify/signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        try:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                try:
                    user = UserDetail.objects.get(username=username)
                    if user.password == password:
                        return JsonResponse({
                            "success": True,
                            "message": "Login successful!"
                        }, status=200)
                    else:
                        return JsonResponse({
                            "error": "Invalid password"
                        }, status=400)
                except UserDetail.DoesNotExist:
                    return JsonResponse({
                        "error": "Username not found"
                    }, status=404)
        except Exception as e:
            return JsonResponse({
                "error": str(e),
            }, status=500)
    else:
        form = LoginForm()
    return render(request, "Loginify/login.html", {"form": form})