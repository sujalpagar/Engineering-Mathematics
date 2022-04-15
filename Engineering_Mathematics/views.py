from django.shortcuts import render

def starting(request):
    return render(request,'index.html')

def Engineering_Mathematics(request):
    return render(request,'homepage.html')

