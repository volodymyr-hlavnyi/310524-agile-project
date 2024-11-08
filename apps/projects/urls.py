from django.urls import path, include
from .views.project_views import *
from .views.project_file_views import *

urlpatterns = [
    path('projects/', ProjectsApi.as_view()),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view()),
    path('files/', ProjectFileListAPIView.as_view()),
]