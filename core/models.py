from calendar import c
from django.db import models
from uuid import uuid4

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)