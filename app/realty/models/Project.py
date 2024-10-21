from django.db.models import CharField, Model


class Project(Model):
    name = CharField(
        verbose_name='Имя',
        max_length=100,
    )

    def __str__(self):
        return self.name
