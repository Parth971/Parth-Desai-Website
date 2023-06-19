from django.contrib import admin

from blog.models import Category, Post, Comment, BlogMetaData

admin.site.register([Category, Post, Comment, BlogMetaData])
