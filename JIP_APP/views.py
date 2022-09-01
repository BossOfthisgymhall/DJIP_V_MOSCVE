from django.shortcuts import render

def STARTUEM(request):
    return render(request, 'STARTUEM.html')

def main(request):
    return render(request, 'main.html')

