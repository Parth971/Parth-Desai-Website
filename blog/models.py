from django.db import models

from accounts.models import User
from blog.utils import upload_post_image


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_post_image)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.title = "_".join(self.title.lower().split(' '))
        super(Post, self).save(**kwargs)


class Comment(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
