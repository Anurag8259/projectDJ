from django.contrib import admin
from hardware.models import Hardware
# Register your models here.
class HardwareForm(admin.ModelAdmin):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['asset_id','hardware_name','allotment','status'].required=True
class HardwareAdmin(admin.ModelAdmin):
    list_display=('asset_id','hardware_name','buy_date','price','warranty','allotment','status')

# model_list=[Hardware,Softwares]
admin.site.register(Hardware,HardwareAdmin)
    
# admin.site.register(Hardware,HardwareAdmin)
