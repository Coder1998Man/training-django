from django.urls import path
from .views import projects, project, create_project_form

urlpatterns = [
    path('', projects, name='home'),
    path('create_project_form/', create_project_form, name='create_project'),
    path('project/<uuid:pk>/', project, name='project'),
]
