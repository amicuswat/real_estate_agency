from django.contrib import admin

from .models import Flat

class AdminFlat(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)


admin.site.register(Flat, AdminFlat)
