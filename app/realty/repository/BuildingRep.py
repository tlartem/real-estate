from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from realty.models import Building


def get_building(building_id: int) -> Building:
    building = get_object_or_404(Building, pk=building_id)
    return building


def get_building_list() -> QuerySet:
    buildings = Building.objects.all().prefetch_related('flats')
    return buildings
