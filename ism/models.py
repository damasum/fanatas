from django.db import models

# Create your models here.
class Student(models.Model):
    Name= models.CharField(max_length=100)
    Email=models.EmailField()
    Roll_no=models.IntegerField()
    Phone_no=models.IntegerField()
    Address=models.CharField(max_length=200)