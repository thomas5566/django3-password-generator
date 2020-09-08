from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, "generator/home.html")


def password(request):

    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get("uppercase"):
        characters.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    if request.GET.get("special"):
        characters.extend("!@#$%^&*()")

    if request.GET.get("numbers"):
        characters.extend("0123456789")

    length = int(request.GET.get("length", 12))

    thepassword = ""

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {"password": thepassword})


def about(request):
    myage = 37
    return render(request, "generator/about.html", {"age": myage})
