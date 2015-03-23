from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # User built-in model
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Basically toString()
    def __unicode__(self):
        return self.user.username