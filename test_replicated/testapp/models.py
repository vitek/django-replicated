from django.db import models

# Create your models here.
class Stat(models.Model):
    clicks = models.IntegerField(default=0)
    shows = models.IntegerField(default=0)
