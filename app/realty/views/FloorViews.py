from rest_framework.relations import SlugRelatedField
from rest_framework.response import Response
from rest_framework.serializers import (
    CharField,
    DecimalField,
    IntegerField,
    Serializer,
)
from rest_framework.views import APIView

from realty.models import Flat, Floor
from realty.repository import FloorRep


class FlatsOnFloorView(APIView):
    class FlatsOnFloorSerializer(Serializer):
        number = IntegerField()
        building = CharField()

        class FlatsMinSerializer(Serializer):
            id = IntegerField()
            rooms = IntegerField(source='plan.rooms')
            price = DecimalField(max_digits=10, decimal_places=2)
            project = SlugRelatedField('name', read_only=True)
            building = SlugRelatedField('name', read_only=True)

            class Meta:
                model = Flat

        flats = FlatsMinSerializer(many=True, read_only=True)

        class Meta:
            model = Floor

    serializer_class = FlatsOnFloorSerializer

    def get(self, request, building_id=None, floor_number=None):
        floor = FloorRep.get_floor_by_building_and_number(building_id, floor_number)
        serializer = self.FlatsOnFloorSerializer(floor)
        return Response(serializer.data)
