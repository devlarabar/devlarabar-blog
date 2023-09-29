from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=20, blank=True))

    def __str__(self):
        return self.title
