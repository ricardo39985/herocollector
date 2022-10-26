from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('heroes')
    return render(request, 'home.html')


def heroes(request):

    return render(request, 'heroes.html')
