from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnersFlatsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('flat', 'owner')


@admin.register(Flat)
class AdminFlat(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)
    inlines = [OwnersFlatsInline]


@admin.register(Complaint)
class AdminComplaint(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat', )


@admin.register(Owner)
class AdminOwner(admin.ModelAdmin):
    list_display = ('name', 'pure_phone', 'phonenumber')
    raw_id_fields = ('flats',)


# admin.site.register(Flat, AdminFlat)
# admin.site.register(Complaint, AdminComplaint)
# admin.site.register(Owner, AdminOwner)
