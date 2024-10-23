from django.contrib import admin

from realty.models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'floor',
        'section',
        'project',
        'building',
        'plan_image',
        'plan',
    )
    list_display_links = ('id',)
    search_fields = (
        'plan__rooms',
        'floor__number',
        'section__name',
        'project__name',
        'building__name',
    )
    list_filter = (
        'floor__number',
        'section__name',
        'project__name',
        'building__name',
    )
    list_editable = ()
    list_per_page = 20

    def plan_image(self, obj):
        return obj.plan.image

    plan_image.short_description = 'Фото планировки'
