from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    born_at = models.DateField()
    alias = models.CharField(max_length=100)
    def __str__(self):
        return self.name
