from django.core.validators import FileExtensionValidator
from django.db.models import CharField, ImageField, Model, TextField


class Project(Model):
    name = CharField(
        verbose_name='Имя',
        max_length=100,
    )
    description = TextField(verbose_name='Описание', blank=True, null=True)
    address = CharField(verbose_name='Адрес', max_length=255)
    metro = CharField(verbose_name='Метро', max_length=100)
    image = ImageField(
        verbose_name='Изображение',
        upload_to='projects/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
