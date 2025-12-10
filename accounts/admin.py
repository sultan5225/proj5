from django.contrib import admin
from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "phone", "city", "region", "is_default")
    list_filter = ("city", "region", "is_default")
    search_fields = ("user__username", "full_name", "phone")
