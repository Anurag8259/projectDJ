from django.db import models

# Create your models here.
class Location(models.Model):
    # location_id=models.CharField(max_length=20,default=0)
    location_name = models.CharField(max_length=50,primary_key=True)
    pincode=models.IntegerField(default=0)
    def __str__(self):
        return self.location_name