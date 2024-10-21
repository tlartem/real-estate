from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from realty.models import Flat
from realty.serializers import FlatDetailSerializer, FlatListSerializer


class FlatDetailView(APIView):
    def get(self, request, flat_pk=None):
        flat = get_object_or_404(Flat.objects.all(), pk=flat_pk)
        serializer = FlatDetailSerializer(flat)
        return Response(serializer.data)


class FlatListView(APIView):
    def get(self, request):
        serializer = FlatListSerializer(Flat.objects.all(), many=True)
        return Response(serializer.data)
