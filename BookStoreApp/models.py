from django.db import models

# Create your models here.

class BookDB(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    lang = models.CharField(max_length=15)