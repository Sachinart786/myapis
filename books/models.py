from django.db import models

# Create your models here.

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
