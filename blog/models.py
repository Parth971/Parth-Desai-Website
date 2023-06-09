from django.db import models

from accounts.models import User
from blog.utils import upload_post_image, upload_blog_meta_data_image

from ckeditor.fields import RichTextField 


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_post_image)
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class BlogMetaData(models.Model):
    image = models.ImageField(upload_to=upload_blog_meta_data_image)
