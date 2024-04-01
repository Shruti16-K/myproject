from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    user = "shruti"
    product_numb = 4
    return render(request, "styling/home.html", {"name": user, "product": product_numb,})

def signup(request):
    return render(request, "styling/signup.html")

def greet(request, user):
    if user == "Sir" or user == "Ma'am":
        return HttpResponse(f"Hello, {user}!")
    else:
        return HttpResponse("Sorry this page is not available;(")

