from django.contrib import admin

from realty.models import Building, Flat, Floor, Plan, Project, Section


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin): ...


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin): ...


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin): ...


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin): ...


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin): ...


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin): ...
