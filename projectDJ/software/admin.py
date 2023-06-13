from django.contrib import admin
from software.models import Software
# Register your models here.
class SoftwareAdmin(admin.ModelAdmin):
    list_display=('software_name','buy_date','price','version','vendor','validity')

admin.site.register(Software,SoftwareAdmin)