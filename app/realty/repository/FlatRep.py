from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from realty.models import Flat


def get_flat(flat_id: int) -> Flat:
    flat = get_object_or_404(Flat, pk=flat_id)
    return flat


def get_flat_list() -> QuerySet[Flat]:
    flats = Flat.objects.all()
    return flats
