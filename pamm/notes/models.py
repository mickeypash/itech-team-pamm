from django.db import models
# from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Note(models.Model):
    title = models.CharField(max_length=200)
    #author = models.ForeignKey(User)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField('Tag', related_name='notes', blank=True)

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    label = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.label


class Folder(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    note = models.ManyToManyField(Note)

    def __unicode__(self):
        return self.title

from django.db import models

# Create your models here.
# class Note(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     tags = models.ManyToManyField('Tag', related_name='notes', blank=True)
#
#     def __unicode__(self):
#         return self.title
#
#
# class Tag(models.Model):
#     label = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=50)
#     def __unicode__(self):
#         return self.label