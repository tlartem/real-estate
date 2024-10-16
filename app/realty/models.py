from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)


class Realty(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="realities"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True


class Building(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="buildings"
    )


class Flat(Realty):
    rooms = models.IntegerField()
    area = models.IntegerField()
    floor = models.IntegerField()
    settlement_before = models.DateField()
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="flats"
    )
