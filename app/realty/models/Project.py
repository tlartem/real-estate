from django.db.models import CharField, Model, TextField


class Project(Model):
    name = CharField(
        verbose_name='Имя',
        max_length=100,
    )
    description = TextField(verbose_name='Описание', blank=True, null=True)
    address = CharField(verbose_name='Адрес', max_length=255)
    metro = CharField(verbose_name='Метро', max_length=100)

    def __str__(self):
        return self.name
