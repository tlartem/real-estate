from django.contrib import admin

from ..models.Building import Building


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'project_name',
        'address',
        'image',
        'flats_count',
        'total_floors',
        'settlement_before',
    )
    search_fields = ('name',)
    list_filter = (
        'project',
        'settlement_before',
    )

    def project_name(self, obj):
        return obj.project.name

    project_name.short_description = 'Проект'

    def flats_count(self, obj):
        return obj.flats.count()

    flats_count.short_description = 'Количество квартир'

    def total_floors(self, obj):
        return obj.floors.count()

    total_floors.short_description = 'Количество этажей'
