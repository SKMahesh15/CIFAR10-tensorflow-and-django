import os
from django.db import models
from .storage import OverwriteStorage

def image_path(instance, filename):
        return os.path.join('image', 'image.jpg')

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to=image_path, storage=OverwriteStorage())

    def __str__(self):
        return self.image.url
    