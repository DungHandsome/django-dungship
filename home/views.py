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

def labs(request):
    data = {
        'tag':Tags.objects.all().order_by('-tag_slug'),
        'lab':Labs.objects.all().order_by('-date'),
    }
    return render(request, 'home/lab/labs.html', data)

def lab_page(request, slug):
    data = {
        'lab':Labs.objects.get(lab_slug=slug),
        'tag':Tags.objects.all().order_by('-tag_slug'),
    }
    return render(request, 'home/lab/lab_page.html', data)

def tags(request):
    data = {
        'tag':Tags.objects.all().order_by('-tag_slug'),
    }
    return render(request, 'home/tag/tags.html', data)

def tag_page(request, slug):
    data = {
        'tag':Tags.objects.get(tag_slug=slug),
        'tag_course': Courses.objects.filter(course_tags__tag_slug=slug).order_by('-date'), 
        'tag_lab': Labs.objects.filter(lab_tags__tag_slug=slug).order_by('-date'),
    }
    print(Courses.objects.filter(course_tags__tag_slug=slug).order_by('-date'))
    return render(request, 'home/tag/tag_page.html', data)