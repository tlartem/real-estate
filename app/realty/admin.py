from django.contrib import admin

from realty.models import Building, Flat, Project


class FlatAdmin(admin.ModelAdmin):
    pass


class BuildingAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Flat, FlatAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Project, ProjectAdmin)
