from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import projects, project, create_project, update_project, delete_project

urlpatterns = [
    path('', projects, name='home'),
    path('create_project_form/', create_project, name='create_project'),
    path('/project/<str:pk>/', project, name='project'),
    path('update_project/<str:pk>/', update_project, name='update_project'),
    path('delete_project/<str:pk>/', delete_project, name='delete_project'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
