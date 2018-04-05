from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=10000)
    author = models.ForeignKey('auth.User')
    publishing_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-publishing_date']

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey("Post", related_name="comments")
    author = models.ForeignKey("auth.User")
    text = models.TextField(max_length=550)
    publishing_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-publishing_date"]

    def __str__(self):
        return self.text

class Choice(models.Model):
    NAMES_CHOICES = (
    ('J', 'Jack'),
    ('P', 'Pes'),
    )
    name = models.CharField(max_length=50)
    choices = models.CharField(max_length=1, choices=NAMES_CHOICES)
