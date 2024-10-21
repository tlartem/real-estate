from django.core.validators import MinValueValidator
from django.db.models import (
    CASCADE,
    CharField,
    DecimalField,
    ForeignKey,
    ImageField,
    Model,
    TextField,
)

from .Project import Project


class Realty(Model):
    image = ImageField(
        verbose_name='Изображение',
    )

    description = TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )

    price = DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    STATUS_CHOICES = [
        ('On sale', 'В продаже'),
        ('Sold', 'Продана'),
    ]

    status = CharField(
        verbose_name='Статус',
        max_length=7,
        choices=STATUS_CHOICES,
        default='On sale',
    )

    project = ForeignKey(
        verbose_name='Проект',
        to=Project,
        on_delete=CASCADE,
        related_name='realities',
    )

    def __str__(self):
        return f'{self.project}:'

    class Meta:
        abstract = True
