from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=55)
    price = models.IntegerField(null=False)
    description = models.TextField(null = True)

    def __str__(self):
        return f'{self.title} -> {self.price}'
    
class Item2(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete = models.CASCADE,
        related_name='item'
        )