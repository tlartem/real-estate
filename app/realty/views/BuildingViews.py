from rest_framework.response import Response
from rest_framework.serializers import (
    CharField,
    ImageField,
    IntegerField,
    Serializer,
    SlugRelatedField,
)
from rest_framework.views import APIView

from realty.models import Building, Flat
from realty.repository import BuildingRep, FlatRep


class BuildingListView(APIView):
    class BuildingListSerializer(Serializer):
        name = CharField()
        address = CharField()
        project = SlugRelatedField(slug_field='name', read_only=True)

        class Meta:
            model = Building

    serializer_class = BuildingListSerializer

    def get(self, request):
        serializer = self.serializer_class(BuildingRep.get_building_list(), many=True)
        return Response(serializer.data)


class BuildingDetailView(APIView):
    class BuildingDetailSerializer(Serializer):
        name = CharField()
        address = CharField()
        project = SlugRelatedField(slug_field='name', read_only=True)
        image = ImageField()
        total_flats = IntegerField(source='flats.count', read_only=True)
        total_floors = IntegerField(source='floors.count', read_only=True)

        class FlatListSerializer(Serializer):
            id = IntegerField()
            rooms = IntegerField(source='plan.rooms')
            floor = SlugRelatedField('number', read_only=True)
            section = SlugRelatedField('name', read_only=True)

            class Meta:
                model = Flat

        flats = FlatListSerializer(FlatRep.get_flat_list(), many=True)

        class Meta:
            model = Building

    serializer_class = BuildingDetailSerializer

    def get(self, request, building_id):
        building = BuildingRep.get_building(building_id)
        serializer = self.serializer_class(building)
        return Response(serializer.data)
