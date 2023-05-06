from django.urls import path

from blog.views import BlogDetailView

urlpatterns = [
    path("<int:blog_id>", BlogDetailView.as_view(), name='blog_detail'),
]
