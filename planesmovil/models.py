from django.db import models
from django.contrib.auth.models import User

class Plan_movil(models.Model):
    title = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)
    description = models.TextField()
    publishedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)