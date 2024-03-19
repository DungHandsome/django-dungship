from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('courses/', courses, name='courses'),
    path('courses/<slug:slug>', course_page, name='course_page'),
]