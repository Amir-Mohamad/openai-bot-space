from django.db import models
from common.models import BaseModel
from django.contrib import admin


class Bot(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='bots')
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name