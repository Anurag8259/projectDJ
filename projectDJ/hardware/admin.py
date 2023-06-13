from django.contrib import admin
from hardware.models import Hardware
# Register your models here.
class HardwareAdmin(admin.ModelAdmin):
    list_display=('asset_id','hardware_name','location','buy_date','price','warranty','allotment','status','softwares')

# model_list=[Hardware,Softwares]
admin.site.register(Hardware,HardwareAdmin)
    
# admin.site.register(Hardware,HardwareAdmin)
