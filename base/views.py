from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def product(request):
     return render(request, 'base/product.html')
