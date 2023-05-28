from django.db import models

from dashboard.utils import upload_skill_logo


class Skill(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=upload_skill_logo)
    link = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
