# Generated by Django 5.0.3 on 2024-03-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_courses_date_labs_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_image',
            field=models.ImageField(blank=True, null=True, upload_to='courses_images/'),
        ),
        migrations.AlterField(
            model_name='labs',
            name='lab_image',
            field=models.ImageField(blank=True, null=True, upload_to='labs_images/'),
        ),
    ]