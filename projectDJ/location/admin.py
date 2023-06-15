
from django.contrib import admin
from .models import Location
# Register your models here.
class LocationForm(admin.ModelAdmin):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['location_name','pincode'].required=True

class LocationAdmin(admin.ModelAdmin):
    list_display=('location_name','pincode')
admin.site.register(Location,LocationAdmin)