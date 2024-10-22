from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import (
    CharField,
    DateField,
    DecimalField,
    FloatField,
    ImageField,
    IntegerField,
    Serializer,
    SlugRelatedField,
)
from rest_framework.views import APIView

from realty.models import Flat


class FlatDetailView(APIView):
    class FlatDetailSerializer(Serializer):
        project = SlugRelatedField('name', read_only=True)
        building = SlugRelatedField('name', read_only=True)
        floor = SlugRelatedField('number', read_only=True)
        section = SlugRelatedField('name', read_only=True)
        image = ImageField()
        description = CharField()
        price = DecimalField(max_digits=10, decimal_places=2)
        status = CharField()
        rooms = IntegerField()
        area = FloatField()
        kitchen_area = FloatField()
        settlement_before = DateField()

        class Meta:
            model = Flat

    serializer_class = FlatDetailSerializer

    def get(self, request, flat_pk=None):
        flat = get_object_or_404(Flat.objects.all(), pk=flat_pk)
        serializer = self.FlatDetailSerializer(flat)
        return Response(serializer.data)


class FlatListView(APIView):
    class FlatListSerializer(Serializer):
        id = IntegerField()
        rooms = IntegerField()
        floor = SlugRelatedField('number', read_only=True)
        section = SlugRelatedField('name', read_only=True)
        project = SlugRelatedField('name', read_only=True)
        building = SlugRelatedField('name', read_only=True)

        class Meta:
            model = Flat

    serializer_class = FlatListSerializer

    def get(self, request):
        serializer = self.FlatListSerializer(Flat.objects.all(), many=True)
        return Response(serializer.data)
