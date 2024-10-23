from django.contrib import admin
from django.db.models import Count

from realty.models.Project import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'address',
        'metro',
        'total_buildings',
        'total_flats',
    )
    search_fields = ('name',)
    list_filter = ('address', 'metro')

    def total_buildings(self, obj):
        return obj.buildings.count()

    total_buildings.short_description = 'Количество корпусов'

    def total_flats(self, obj):
        return obj.buildings.aggregate(total_flats=Count('flats'))['total_flats'] or 0

    total_flats.short_description = 'Количество квартир'
