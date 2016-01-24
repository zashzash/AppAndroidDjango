from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

# Create your models here.


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 50, blank = True, null = True)
    description = models.CharField(max_length = 300, blank = True, null = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET(get_sentinel_user))

    def __unicode__(self): #Python 3.3 is __self__
        return self.title

    def __str__(self):
        return self.title
