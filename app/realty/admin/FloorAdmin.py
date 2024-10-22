from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realty.models import Floor


@admin.register(Floor)
class FloorAdmin(ModelAdmin):
    list_display = (
        'id',
        'number',
        'get_flats_count',
        'building_project',
        'get_total_area',
    )
    search_fields = ('number', 'building_project')
    list_filter = (
        'building__project',
        'number',
    )

    def building_project(self, obj):
        return obj.building.project

    building_project.short_description = 'Проект'

    def get_flats_count(self, obj):
        return obj.flats.count()

    get_flats_count.short_description = 'Количество квартир'

    def get_total_area(self, obj):
        return sum(flat.plan.area for flat in obj.flats.all())

    get_total_area.short_description = 'Общая площадь'
