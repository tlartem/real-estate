from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from realty.models import Building, Flat, Floor, Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class BuildingSerializer(ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class FlatDetailSerializer(ModelSerializer):
    project = SlugRelatedField(
        slug_field='name',
        queryset=Project.objects.all(),
    )

    building = SlugRelatedField(
        slug_field='name',
        queryset=Building.objects.all(),
    )

    floor = SlugRelatedField(
        slug_field='number',
        queryset=Floor.objects.all(),
    )

    class Meta:
        model = Flat
        fields = '__all__'


class FlatListSerializer(ModelSerializer):
    project = SlugRelatedField(slug_field='name', queryset=Project.objects.all())
    building = SlugRelatedField(slug_field='name', queryset=Building.objects.all())

    class Meta:
        model = Flat
        fields = ['id', 'rooms', 'price', 'project', 'building']


class FlatsOnFloorSerializer(ModelSerializer):
    flats = FlatListSerializer(many=True, read_only=True)

    class Meta:
        model = Floor
        fields = ['id', 'number', 'building', 'flats']
