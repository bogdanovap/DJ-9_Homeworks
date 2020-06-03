from django.contrib import admin

# Register your models here.
from phones.models import Vendor, Phone

class VendorAdmin(admin.ModelAdmin):
    pass

class PhoneAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Phone, PhoneAdmin)