from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    education = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    section = models.CharField(max_length=10)
    roll_no = models.IntegerField(max_length=100)



