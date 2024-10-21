from django.core.validators import MinValueValidator
from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    DecimalField,
    FloatField,
    ForeignKey,
    ImageField,
    Model,
    PositiveSmallIntegerField,
    TextField,
)


class Project(Model):
    name = CharField(
        verbose_name='Имя',
        max_length=100,
    )

    def __str__(self):
        return self.name


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


class Building(Model):
    name = CharField(
        verbose_name='Имя',
        max_length=100,
    )
    project = ForeignKey(Project, on_delete=CASCADE, related_name='buildings')

    def __str__(self):
        return self.name


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

    floor = PositiveSmallIntegerField(
        verbose_name='Этаж',
    )

    settlement_before = DateField(
        verbose_name='Заселение после',
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
            f'Этаж: {self.floor}, '
            f'Комнат: {self.rooms}'
        )
