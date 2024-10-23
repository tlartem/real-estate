from django.core.validators import FileExtensionValidator
from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    ForeignKey,
    ImageField,
    Model,
)

from .Project import Project


class Building(Model):
    name = CharField(
        verbose_name='Имя',
        max_length=100,
    )
    image = ImageField(
        verbose_name='Картинка корпуса',
        upload_to='buildings/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
    )
    address = CharField(verbose_name='Адрес', max_length=255)
    project = ForeignKey(Project, on_delete=CASCADE, related_name='buildings')

    settlement_before = DateField(
        verbose_name='Срок сдачи',
    )

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'

    def __str__(self):
        return self.name
