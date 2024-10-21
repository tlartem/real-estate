from django.db.models import CASCADE, CharField, ForeignKey, Model

from .Building import Building


class Section(Model):
    name = CharField(verbose_name='Название', max_length=50)

    building = ForeignKey(
        verbose_name='Корпус', to=Building, on_delete=CASCADE, related_name='sections'
    )

    def __str__(self) -> str:
        return f'Секция {self.name}, корпус {self.building}'
