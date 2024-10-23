from django.contrib import admin

from ..models.Section import Section


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'get_flats_count',
        'building',
        'building_project',
    )
    search_fields = ('name',)

    def building_project(self, obj):
        return obj.building.project

    building_project.short_description = 'Проект'

    def get_flats_count(self, obj):
        return obj.flats.count()

    get_flats_count.short_description = 'Количество квартир'
