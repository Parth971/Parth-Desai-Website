from django.db import models

from project.utils import upload_project_image


class Project(models.Model):
    image = models.ImageField(upload_to=upload_project_image)
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.title
    