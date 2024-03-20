from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def courses(request):
    data = {
        'tag':Tags.objects.all().order_by('-tag_slug'),
        'course':Courses.objects.all().order_by('-date'),
        #'lab':Labs.objects.all().order_by('-date'),
    }
    return render(request, 'home/course/courses.html', data)

def course_page(request, slug):
    data = {
        'course':Courses.objects.get(course_slug=slug),
        'tag':Tags.objects.all().order_by('-tag_slug'),
    }
    return render(request, 'home/course/course_page.html', data)