from django.db.models import (
    CASCADE,
    SET_NULL,
    ForeignKey,
)

from .Building import Building
from .Floor import Floor
from .Plan import Plan
from .Realty import Realty
from .Section import Section


class Flat(Realty):
    floor = ForeignKey(
        verbose_name='Этаж',
        to=Floor,
        on_delete=CASCADE,
        related_name='flats',
    )

    section = ForeignKey(
        verbose_name='Секция',
        to=Section,
        on_delete=SET_NULL,
        related_name='flats',
        null=True,
        blank=True,
    )

    building = ForeignKey(
        verbose_name='Корпус',
        to=Building,
        on_delete=CASCADE,
        related_name='flats',
    )

    plan = ForeignKey(
        verbose_name='Планировка',
        to=Plan,
        on_delete=CASCADE,
        related_name='flats',
    )

    def __str__(self):
        return (
            f'{self.building.project}, '
            f'Корпус: {self.building}, '
            f'{self.floor}, '
            f'Комнат: {self.plan.rooms}'
        )
