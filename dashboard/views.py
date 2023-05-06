from django.views.generic import TemplateView

from blog.models import Post
from dashboard.models import Skill
from project.models import Project


class HomeView(TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        context['projects'] = Project.objects.all()
        context['blogs'] = Post.objects.all()[:6]
        return context
