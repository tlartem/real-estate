from django.core.validators import MinValueValidator
from django.db.models import (
    CASCADE,
    SET_NULL,
    DateField,
    FloatField,
    ForeignKey,
    PositiveSmallIntegerField,
)

from .Building import Building
from .Floor import Floor
from .Realty import Realty
from .Section import Section


class Flat(Realty):
    rooms = PositiveSmallIntegerField(
        verbose_name='Кол-во комнат',
    )

    area = FloatField(
        verbose_name='Площадь',
        validators=[MinValueValidator(0)],
    )

    kitchen_area = FloatField(
        verbose_name='Кухня',
        validators=[MinValueValidator(0)],
    )

    floor = ForeignKey(verbose_name='Этаж', to=Floor, on_delete=CASCADE, related_name='flats')

    settlement_before = DateField(
        verbose_name='Заселение после',
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

    def __str__(self):
        return (
            f'{self.building.project}, '
            f'Корпус: {self.building}, '
            f'{self.floor}, '
            f'Комнат: {self.rooms}'
        )
