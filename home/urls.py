from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls, name='admin'),

    # Homepage
    path('', home, name='home'),

    # Course
    path('courses/', courses, name='courses'),
    path('courses/<slug:slug>', course_page, name='course_page'),
    
    # Lab
    path('labs/', labs, name='labs'),
    path('labs/<slug:slug>', lab_page, name='lab_page'),
]