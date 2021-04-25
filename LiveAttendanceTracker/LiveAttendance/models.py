from django.db import models

class Student(models.Model):
    RegdNo = models.CharField(unique=True, max_length=10)
    Email = models.CharField(unique=True, max_length=50)
    Branch = models.CharField(max_length=40)
    Batch = models.CharField(max_length=10)
    Section = models.CharField(max_length=20)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.Password

class Teacher(models.Model):
    TeacherId = models.CharField(unique=True, max_length=15)
    Email = models.CharField(unique=True, max_length=50)
    Branch = models.CharField(max_length=40)
    Password = models.CharField(max_length=30)
    def __str__(self):
        return self.Password