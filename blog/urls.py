from django.urls import path

from blog.views import BlogDetailView, BlogListView

urlpatterns = [
    path("<int:blog_id>", BlogDetailView.as_view(), name='blog_detail'),
    path("", BlogListView.as_view(), name='blog_list'),
]
