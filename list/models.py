from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)
    color = models.CharField(max_length=30)

class ToDo(models.Model):
    name = models.CharField(max_length=60)
    achieved = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


