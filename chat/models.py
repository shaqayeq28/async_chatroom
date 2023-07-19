from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(verbose_name='chat room name', max_length=255)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(verbose_name='is active', default=True)

    def __str__(self):
        return self.name
