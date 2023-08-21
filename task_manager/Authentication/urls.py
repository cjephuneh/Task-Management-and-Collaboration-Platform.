from django.urls import path
from .views import UserRegistrationView, UserLoginView, LogoutView, UserListView, UserProfileView, PasswordResetView, PasswordResetConfirmView
# PasswordChangeView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('password/reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    # path('password/change/', PasswordChangeView.as_view(), name='password-change'),
]
