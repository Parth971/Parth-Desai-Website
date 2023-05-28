from django.views.generic import DetailView, ListView

from blog.models import Post, Category
from core.mixins import PaginationMixin
from core.utils import CustomPaginator


class BlogDetailView(DetailView):
    template_name = 'blog/detail.html'
    context_object_name = 'blog'
    model = Post
    pk_url_kwarg = 'blog_id'


class BlogListView(PaginationMixin, ListView):
    template_name = 'blog/list_blogs.html'
    context_object_name = 'blogs'
    model = Post
    ordering = ['-id']
    paginator_class = CustomPaginator

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

