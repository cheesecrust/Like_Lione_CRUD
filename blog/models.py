from distutils.command.upload import upload
from importlib.resources import contents
from venv import create
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=20)
    contents = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/", blank='True', null="True")

    def __str__(self):
        return self.title

    def summary(self):
        return self.contents[:100]
