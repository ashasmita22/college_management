from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(100)
    gender = models.CharField(5)
    address = models.CharField(100)
    standard = models.CharField(10)
    phone_number = models.IntegerField()
    class_teacher = models.CharField(100)
    father_name = models.CharField(100)
    email = models.CharField(100)



class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(100)
    gender = models.CharField(5)
    address = models.CharField(100)
    subject = models.CharField(50)
    phone_number = models.IntegerField()
    email = models.CharField(100)


class Admin(AbstractUser):
    email = models.CharField(100)
    name = models.CharField(100)
    phone_number = models.IntegerField()
    job_level =  models.IntegerField()
    address = models.CharField(100)

class TimeTable(models.Model):
    period = models.ForeignKey(Period , on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE, null=True, blank=True)
    day = models.CharField(20)
    standard = models.CharField(20)

class Subject(models.Model):
    id = models.IntegerField()
    subject = models.CharField(20)

class Period(models.Model):
    period = models.IntegerField()
