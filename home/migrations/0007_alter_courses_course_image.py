# Generated by Django 5.0.3 on 2024-03-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_courses_course_image_alter_labs_lab_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_image',
            field=models.FileField(blank=True, null=True, upload_to='courses_images'),
        ),
    ]
