from django.views.generic import ListView

from core.mixins import PaginationMixin
from core.utils import CustomPaginator
from project.models import Project


class ProjectListView(PaginationMixin, ListView):
    template_name = 'project/list_projects.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['-id']
    paginator_class = CustomPaginator
    paginate_by = 8

