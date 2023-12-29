from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.TextField()

    def __str__(self):
        return self.user.username

class Article(models.Model):
    title = models.CharField(max_length=200)
    content=models.TextField()

    def __str__(self):
        return self.title