from django.shortcuts import render

def home(request):
    return render(request, 'productos/home.html')

def acerca_de(request):
    return render(request, 'productos/acerca-de-mi.html')