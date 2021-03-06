from django.contrib import admin

from .models import AnnualLeave, SickLeave, Staff

# Register your models here.


class StaffAdmin(admin.ModelAdmin):
    # Admin display
    list_display = (
        "first_name",
        "last_name",
        "email_address",
    )
    # Ordering in admin
    ordering = ("id",)


admin.site.register(Staff, StaffAdmin)
admin.site.register(SickLeave)
admin.site.register(AnnualLeave)
