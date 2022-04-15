from django.shortcuts import render,redirect

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def Mathematics1(request):
    return render(request,'Mathematics-1.html')

def Mathematics2(request):
    return render(request,'Mathematics-2.html')

def Mathematics3(request):
    return render(request,'Mathematics-3.html')

def redirecting(request):
    return redirect("http://127.0.0.1:8000/Engineering_Mathematics/")