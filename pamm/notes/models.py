from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    # User built-in model
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

class Folder(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.label

class Tag(models.Model):
    label = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __unicode__(self):
        return self.label

class Note(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User)
    timestamp = models.DateTimeField()
    content = models.TextField(max_length=50)
    tag = models.ForeignKey(Tag)
    is_shared = models.BooleanField(default=False)

    def __unicode__(self):
        return self.label

