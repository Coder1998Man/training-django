from django.urls import path
from .views import projects, project

urlpatterns = [
    path('', projects, name='home'),
    path('project/<int:pk>/', project, name='project'),
]
