from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    # User built-in model
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Basically toString()
    def __unicode__(self):
        return self.user.username

class Tag(models.Model):
    label = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super(Tag, self).save(*args, **kwargs)

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
        return self.title

class Folder(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    note = models.ManyToManyField(Note)

    def __unicode__(self):
        return self.title