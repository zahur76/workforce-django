from django.contrib import admin
from .models import SalarySlip
# Register your models here.


class SalarySlipAdmin(admin.ModelAdmin):
    # Admin display
    list_display = (
        'staff',
        'created_at'            
    )
    # Ordering in admin
    ordering = ('id',)

admin.site.register(SalarySlip, SalarySlipAdmin)
