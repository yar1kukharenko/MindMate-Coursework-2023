from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from records.models import *


# Register your models here.


# admin.site.register(Clients)
# admin.site.register(Methods)
# admin.site.register(Events)
# admin.site.register(Feelings)


# admin.site.register(Therapist)
# admin.site.register(Records)
class RecordsInstanceInline(admin.TabularInline):
    model = Records


@admin.register(Methods)
class MethodsAdmin(ImportExportModelAdmin):
    search_fields = ('name',)


@admin.register(Events)
class EventsAdmin(ImportExportModelAdmin):
    search_fields = ('name',)


@admin.register(Feelings)
class FeelingsAdmin(ImportExportModelAdmin):
    search_fields = ('name',)


@admin.register(Clients)
class ClientsAdmin(ImportExportModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email')
    fields = ('user', 'photo', ('first_name', 'last_name'), 'email')
    inlines = [RecordsInstanceInline]


@admin.register(Therapist)
class TherapistAdmin(ImportExportModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email')
    inlines = [RecordsInstanceInline]
    filter_horizontal = ('methods', 'feelings', 'events',)
    readonly_fields = ('description',)


@admin.register(Records)
class RecordsAdmin(ImportExportModelAdmin):
    list_display = ('therapist', 'client', 'date', 'price')
    list_filter = ('date', 'price')
    date_hierarchy = 'date'
    list_display_links = ('client',)
    raw_id_fields = ('client', 'therapist',)
