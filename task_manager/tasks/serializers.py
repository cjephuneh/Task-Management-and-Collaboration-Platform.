from rest_framework import serializers
from .models import TaskModel



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'
        read_only_fields = ('created_at', 'completed_at', 'created_by', 'project', 'assigned_to')

        