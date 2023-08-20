from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('api/signup/', views.UserRegistrationAPIView.as_view(), name='api-signup'),
    path('api/login/', views.UserLoginAPIView.as_view(), name='api-login'),
    # Define URLs for profile management, logout, etc.
]
