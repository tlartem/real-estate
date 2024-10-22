from django.db.models import (
    CASCADE,
    CharField,
    ForeignKey,
    Model,
)

from .Project import Project


class Building(Model):
    name = CharField(
        verbose_name='Имя',
        max_length=100,
    )
    address = CharField(verbose_name='Адрес', max_length=255)
    project = ForeignKey(Project, on_delete=CASCADE, related_name='buildings')

    def __str__(self):
        return self.name
