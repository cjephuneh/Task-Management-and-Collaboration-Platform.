from django.urls import path
from .views import UserListView, UserDetailView, UserRegistrationView, UserProfileView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),

    # Additional Endpoints
    path('login/', obtain_auth_token, name='user-login'),  # Obtain authentication token
    path('logout/', LogoutView.as_view(), name='user-logout'),  # Implement your logout view
    path('password/reset/', PasswordResetView.as_view(), name='password-reset'),  # Implement your password reset view
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),  # Implement your password reset confirmation view
    path('password/change/', PasswordChangeView.as_view(), name='password-change'),  # Implement your password change view
]
