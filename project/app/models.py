from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Salesforce(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    instance_url = models.URLField()

    def __str__(self):
        return self.instance_url
