from django.urls import path
from .views import projects_list, project_detail

urlpatterns = [
    path('', projects_list, name='projects'),
    path('<int:id>/', project_detail, name='project_detail'),
]