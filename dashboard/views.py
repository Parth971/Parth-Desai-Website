from django.views.generic import TemplateView

from blog.models import Post
from dashboard.models import Skill
from project.models import Project


class HomeView(TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        context['projects'] = Project.objects.all()[:4]
        context['blogs'] = Post.objects.all()[:3]
        context['social_media'] = {
            'facebook': '',
            'twiter': '',
            'linkedin': '',
            'google': '',
            'github': '',
            'instagram': '',
            'upwork': '',
            'freelancer': '',
        }
        context['cv_url'] = self.request.build_absolute_uri('/media/dashboard/CV2023.pdf')
        return context


class ServicesView(TemplateView):
    template_name = 'dashboard/services.html'