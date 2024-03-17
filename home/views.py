from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def courses(request):
    return render(request, 'home/courses.html')