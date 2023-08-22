from django.db import models


class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    project = models.ForeignKey('Projects.ProjectModel', on_delete=models.CASCADE, null=True, blank=True)
    assigned_to = models.ForeignKey('Authentication.UserModel', on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey('Authentication.UserModel', on_delete=models.CASCADE, related_name='created_by', null=True, blank=True)
    
    def __str__(self):
        return self.title

