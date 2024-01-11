from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

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


class ClientsResource(resources.ModelResource):
    full_name = Field()

    class Meta:
        model = Clients
        fields = ('id', 'first_name', 'last_name', 'full_name', 'email')  # добавляем 'full_name'

    def dehydrate_full_name(self, client):
        # Сконкатенируем имя и фамилию
        return f"{client.first_name} {client.last_name}"


@admin.register(Clients)
class ClientsAdmin(ImportExportModelAdmin):
    resource_class = ClientsResource
    list_display = ('user', 'first_name', 'last_name', 'email')
    fields = ('user', 'photo', ('first_name', 'last_name'), 'email')
    inlines = [RecordsInstanceInline]


@admin.register(Therapist)
class TherapistAdmin(ImportExportModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email')
    inlines = [RecordsInstanceInline]
    filter_horizontal = ('methods', 'feelings', 'events',)
    readonly_fields = ('description',)


class RecordsResource(resources.ModelResource):
    class Meta:
        model = Records
        fields = ('id', 'date', 'time', 'therapist', 'client')

    def dehydrate_date(self, record):
        return record.date.strftime("%d-%m-%Y")


@admin.register(Records)
class RecordsAdmin(ImportExportModelAdmin):
    resource_class = RecordsResource
    list_display = ('therapist', 'client', 'date', 'price')
    list_filter = ('date', 'price')
    date_hierarchy = 'date'
    list_display_links = ('client',)
    raw_id_fields = ('client', 'therapist',)

    def get_export_queryset(self, request):
        queryset = super().get_export_queryset(request)
        return queryset.filter(date__year=datetime.now().year)
