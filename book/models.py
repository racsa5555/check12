from django.db import models
from author.models import Author
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=55)
    genre = models.CharField(max_length=55)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book')


