from django.shortcuts import render
from rest_framework import viewsets


from .models import TaskModel
from .serializers import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer