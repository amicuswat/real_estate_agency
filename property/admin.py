from django.contrib import admin

from .models import Flat, Complaint


class AdminFlat(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)


class AdminComplaint(admin.ModelAdmin):
    raw_id_fields =('user', 'flat', )


admin.site.register(Flat, AdminFlat)
admin.site.register(Complaint, AdminComplaint)
