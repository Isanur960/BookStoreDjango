from django.db import models

# Create your models here.

class BookDB(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    lang = models.CharField(max_length=15)

    def __str__(self):
        return self.name