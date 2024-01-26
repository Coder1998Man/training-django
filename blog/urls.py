from django.urls import path
from .views import projects, project, create_project

urlpatterns = [
    path('', projects, name='projects'),
    path('create_project_form/', create_project, name='create_project'),
    path('project/<uuid:pk>/', project, name='project'),
]
