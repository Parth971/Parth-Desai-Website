from django.views.generic import DetailView

from blog.models import Post


class BlogDetailView(DetailView):
    template_name = 'blog/detail.html'
    context_object_name = 'blog'
    model = Post
    pk_url_kwarg = 'blog_id'
