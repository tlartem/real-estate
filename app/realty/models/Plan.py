from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db.models import FloatField, ImageField, Model, PositiveSmallIntegerField


class Plan(Model):
    image = ImageField(
        verbose_name='Картинка планировки',
        upload_to='plans/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
    )
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

    class Meta:
        verbose_name = 'Планировка'
        verbose_name_plural = 'Планировки'

    def __str__(self):
        return f'Планировка {self.area} м², {self.rooms} комнаты, кухня {self.kitchen_area} м².'
