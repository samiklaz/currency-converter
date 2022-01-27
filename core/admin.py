from django.contrib import admin
from .models import *


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name']


admin.site.register(Currency, CurrencyAdmin)
