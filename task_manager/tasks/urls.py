from django.urls import path
from .views import TaskListAPIView, TaskDetailAPIView

urlpatterns = [
    path('api/tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('api/tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    # Add other URL patterns for other views (create, update, etc.)
]



