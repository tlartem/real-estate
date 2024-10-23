from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import CharField, DateField, IntegerField, Serializer
from rest_framework.views import APIView

from realty.models import Building, Project


class ProjectListView(APIView):
    class ProjectListSerializer(Serializer):
        name = CharField()
        address = CharField()
        metro = CharField()

        class Meta:
            model = Project

    serializer_class = ProjectListSerializer

    def get(self, request):
        projects = Project.objects.all()
        serializer = self.serializer_class(projects, many=True)
        return Response(serializer.data)


class ProjectDetailView(APIView):
    class ProjectDetailSerializer(Serializer):
        name = CharField()
        description = CharField()
        address = CharField()
        metro = CharField()

        total_flats = IntegerField(source='flats.count', read_only=True)
        total_buildings = IntegerField(source='buildings.count', read_only=True)

        class BuildingListSerializer(Serializer):
            id = IntegerField()
            name = CharField()
            settlement_before = DateField()

            class Meta:
                model = Building

        buildings = BuildingListSerializer(Building.objects.all(), many=True)

        class Meta:
            model = Project

    serializer_class = ProjectDetailSerializer

    def get(self, request, project_id=None):
        project = get_object_or_404(Project.objects.all(), pk=project_id)
        serializer = self.ProjectDetailSerializer(project)
        return Response(serializer.data)
