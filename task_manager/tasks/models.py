from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    # Other fields...

# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     due_date = models.DateTimeField()
#     assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     # Other fields...
