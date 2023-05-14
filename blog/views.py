from django.views.generic import DetailView, ListView

from blog.models import Post


class BlogDetailView(DetailView):
    template_name = 'blog/detail.html'
    context_object_name = 'blog'
    model = Post
    pk_url_kwarg = 'blog_id'


class BlogListView(ListView):
    template_name = 'blog/list_blogs.html'
    context_object_name = 'blogs'
    model = Post
