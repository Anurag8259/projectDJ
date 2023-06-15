from hardware.models import Hardware
from django.db import models

# Create your models here.
class Employees(models.Model):
    employee_id=models.CharField(max_length=10,default=0)
    employee_name=models.CharField(max_length=50)
    age=models.IntegerField(default=0)
    hardware=models.ManyToManyField(Hardware)
    
