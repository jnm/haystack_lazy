from django.db import models
from django.conf import settings

# Create your models here.

class FavoriteWord(models.Model):
    word = models.CharField(max_length=123)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
