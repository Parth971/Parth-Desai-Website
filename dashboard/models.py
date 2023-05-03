from django.db import models


def upload_skill_logo(instance, filename):
    extension = filename.split(".")[-1]
    return f'skills/logo/{"_".join(instance.name.lower().split(" "))}.{extension}'


class Skill(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=upload_skill_logo)
    
