from django.db import models
import datetime
# Create your models here.
class Hardware(models.Model):
    asset_id=models.CharField(max_length=50)
    hardware_name=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    price=models.CharField(max_length=15)
    buy_date=models.DateField(default=datetime.date.today)
    warranty=models.IntegerField(default=0)
    allotment=models.CharField(max_length=50,default="null")
    status=models.CharField(max_length=50,default="inactive")
    softwares=models.CharField(max_length=100,default="null")
