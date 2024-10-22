from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from realty.views import (
    BuildingDetailView,
    BuildingListView,
    FlatDetailView,
    FlatListView,
    FlatsOnFloorView,
    ProjectDetailView,
    ProjectListView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
]

flats = [
    path('api/flats/', FlatListView.as_view(), name='flats-list'),
    path('api/flats/<int:flat_pk>/', FlatDetailView.as_view(), name='flat-detail'),
]

buildings = [
    path('api/buildings/', BuildingListView.as_view()),
    path('api/buildings/<int:building_id>/', BuildingDetailView.as_view()),
]

projects = [
    path('api/projects/', ProjectListView.as_view()),
    path('api/projects/<int:project_id>/', ProjectDetailView.as_view()),
]

floor_with_flats = [
    path(
        'buildings/<int:building_id>/floor/<int:floor_number>/',
        FlatsOnFloorView.as_view(),
    )
]

schema = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/schema/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='docs',
    ),
]

urlpatterns += flats + schema + floor_with_flats + buildings + projects
