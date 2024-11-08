from django.urls import path

from apps.users.views.user_views import *

urlpatterns = [
    path('users/', UserListGenericView.as_view(), name='user-list'),
    path('users/register/', RegisterUserGenericView.as_view(), name='user-register'),
]
