from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.filters import DjangoFilterBackend, OrderingFilter
from .models import TaskModel
from .serializers import TaskSerializer



# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer


class TaskListAPIView(generics.ListAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Enable filtering and sorting
    filter_fields = ['status', 'due_date']  # Fields available for filtering
    ordering_fields = ['created_at', 'due_date']  # Fields available for sorting


