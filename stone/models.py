from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    publish_time = models.DateField()

class UserInfo(models.Model):
    user = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    ug = models.CharField(max_length=10)

    def __str__(self):
        return self.name