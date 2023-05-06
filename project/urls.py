from django.urls import path
from project.views import ProjectListView

urlpatterns = [
    path("", ProjectListView.as_view(), name='project_list'),
]
