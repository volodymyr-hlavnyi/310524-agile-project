from django.urls import path
from apps.users.views.user_views import (
    UserListGenericView,
    RegisterUserGenericView,
    UserDetailGenericView
)

urlpatterns = [
    path('users/', UserListGenericView.as_view(), name='user-list'),
    path('users/register/', RegisterUserGenericView.as_view(), name='user-register'),
    path('users/<int:id>/', UserDetailGenericView.as_view(), name='user-detail'),

]
