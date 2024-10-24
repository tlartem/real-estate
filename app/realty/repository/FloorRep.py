from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from realty.models import Floor


def get_floor(floor_id: int) -> Floor:
    floor = get_object_or_404(Floor, pk=floor_id)
    return floor


def get_floor_list() -> QuerySet:
    floors = Floor.objects.all().prefetch_related('building')
    return floors


def get_floor_by_building_and_number(building_id: int, floor_number: int) -> Floor:
    floor = get_object_or_404(Floor, building__id=building_id, number=floor_number)
    return floor
