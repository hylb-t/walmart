from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)