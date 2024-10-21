from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from realty.models import Flat
from realty.serializers import FlatDetailSerializer, FlatListSerializer


class FlatView(viewsets.ViewSet):
    queryset = Flat.objects.all()

    def list(self, request):
        serializer = FlatListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        flat = get_object_or_404(self.queryset, pk=pk)
        serializer = FlatDetailSerializer(flat)
        return Response(serializer.data)
