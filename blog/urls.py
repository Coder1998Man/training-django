from django.urls import path
from .views import projects, project

urlpatterns = [
    path('', projects, name='home'),
    path('project/<uuid:pk>/', project, name='project'),
]
