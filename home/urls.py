from django.urls import path
from .views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

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

    # Tag
    path('tags/', tags, name='tags'),
    path('tags/<slug:slug>', tag_page, name='tag_page'),

    # Logout
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
]