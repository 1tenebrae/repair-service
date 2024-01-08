from django.db import models
from django.contrib.auth.models import User

class RepairRequest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, default='Ожидание')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='engineer', null=True, blank=True)
    solution = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

