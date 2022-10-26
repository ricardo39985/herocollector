from django.shortcuts import render, redirect
import os
import uuid
import boto3

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('heroes')
    return render(request, 'home.html')


def heroes(request):
    if request.method == "POST":

        pass

    return render(request, 'heroes.html')
