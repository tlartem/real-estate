from django.db.models import (
    CASCADE,
    ForeignKey,
    Model,
    SmallIntegerField,
)

from .Building import Building


class Floor(Model):
    number = SmallIntegerField(verbose_name='Номер этажа')
    building = ForeignKey(
        verbose_name='Здание', to=Building, on_delete=CASCADE, related_name='floors'
    )

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'

    def __str__(self) -> str:
        return f'Этаж {self.number}'
