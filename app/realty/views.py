from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from realty.models import Flat, Floor
from realty.serializers import FlatDetailSerializer, FlatListSerializer, FlatsOnFloorSerializer


class FlatDetailView(APIView):
    def get(self, request, flat_pk=None):
        flat = get_object_or_404(Flat.objects.all(), pk=flat_pk)
        serializer = FlatDetailSerializer(flat)
        return Response(serializer.data)


class FlatListView(APIView):
    def get(self, request):
        serializer = FlatListSerializer(Flat.objects.all(), many=True)
        return Response(serializer.data)


class FlatsOnFloorView(APIView):
    def get(self, request, building_id=None, floor_number=None):
        floor = get_object_or_404(
            Floor,
            building__id=building_id,
            number=floor_number,
        )
        serializer = FlatsOnFloorSerializer(floor)
        return Response(serializer.data)
