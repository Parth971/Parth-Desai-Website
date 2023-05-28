import json

from django.http import HttpResponse
from django.views.generic import TemplateView

from blog.models import Post
from dashboard.forms import ContactForm
from dashboard.models import Skill
from project.models import Project


class HomeView(TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        context['projects'] = Project.objects.all()[:4]
        context['blogs'] = Post.objects.order_by('created_at')[:3]
        context['social_media'] = {
            'facebook': 'https://www.facebook.com/profile.php?id=100009073984667',
            'twitter': 'https://twitter.com/desaiparth971/',
            'linkedin': 'https://www.linkedin.com/in/parth971/',
            'github': 'https://github.com/Parth971/',
            'instagram': 'https://www.instagram.com/desaiparth_2000/',
            'upwork': 'https://www.upwork.com/freelancers/~011b51adb453c07b00/',
            'freelancer': 'https://www.freelancer.com/u/desaiparth971/',
        }
        context['cv_url'] = self.request.build_absolute_uri('/media/dashboard/CV2023.pdf')

        return context

    def post(self, request):
        print(request.POST)
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse(status=200, content_type="application/json")

        errors = json.loads(form.errors.as_json())
        key, value = errors.popitem()
        return HttpResponse(value[0]['message'].replace('This', key.title()), status=400, content_type="application/json")


class ServicesView(TemplateView):
    template_name = 'dashboard/services.html'