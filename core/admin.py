from django.contrib import admin
from .models import Phones


# Register your models here.

class AdminPhones(admin.ModelAdmin):
    list_display = ("brand", "model", "imei", "status", "note", "added_date")
    list_filter = ("brand", "model")


admin.site.register(Phones, AdminPhones)
