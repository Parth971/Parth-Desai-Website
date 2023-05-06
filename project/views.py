from django.views.generic import ListView

from project.models import Project


class ProjectListView(ListView):
    template_name = 'project/list_projects.html'
    context_object_name = 'projects'
    model = Project

