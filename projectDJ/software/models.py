from django.db import models
valid_choice=[
    ('yearly','Yearly'),
    ('lifetime','Lifetime')
]
# Create your models here.
class Software(models.Model):
    software_name=models.CharField(max_length=50)
    buy_date=models.DateField()
    price=models.CharField(max_length=15,default=0)
    version=models.CharField(max_length=50,default='NA')
    vendor=models.CharField(max_length=50,default='NA')
    validity=models.CharField(max_length=50,choices=valid_choice,default='Lifetime')
    