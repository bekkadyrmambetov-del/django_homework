from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint


def example_view(requets):
    return HttpResponse(f"This is an axample_view. {randint(1, 1000)}")

def html_view(request):
    return render(request, "base.html")

# Create your views here.
