from django.db import models

# Create your models here.

class Tags(models.Model):
    tag_name = models.CharField(max_length=200, unique=True)
    tag_slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.tag_name
    
class Courses(models.Model):
    course_name = models.CharField(max_length=1000, unique=True)
    course_slug = models.SlugField(max_length=1000, unique=True)
    course_title = models.CharField(max_length=1000)
    course_sub_title = models.CharField(max_length=2000)
    course_image = models.ImageField(upload_to='courses_images/', blank=True)
    course_tags = models.ManyToManyField(Tags, related_name='courses_tags')
    def __str__(self):
        return self.course_name
