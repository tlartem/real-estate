from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import (
    CharField,
    DateField,
    DecimalField,
    FloatField,
    IntegerField,
    Serializer,
    SerializerMethodField,
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
        image = SerializerMethodField(method_name='get_image')
        description = CharField()
        price = DecimalField(max_digits=10, decimal_places=2)
        status = CharField()
        rooms = IntegerField(source='plan.rooms')
        area = FloatField(source='plan.area')
        kitchen_area = FloatField(source='plan.kitchen_area')
        settlement_before = DateField(source='building.settlement_before')

        class Meta:
            model = Flat

        def get_image(self, flat):
            request = self.context.get('request')
            if flat.plan and flat.plan.image:
                if request is not None:
                    return request.build_absolute_uri(flat.plan.image.url)
                return flat.plan.image.url
            return None

    serializer_class = FlatDetailSerializer

    def get(self, request, flat_pk=None):
        flat = get_object_or_404(Flat.objects.all(), pk=flat_pk)
        serializer = self.FlatDetailSerializer(flat, context={'request': request})
        return Response(serializer.data)


class FlatListView(APIView):
    class FlatListSerializer(Serializer):
        id = IntegerField()
        rooms = IntegerField(source='plan.rooms')
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
