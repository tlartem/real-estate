from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from realty.views import FlatDetailView, FlatListView

urlpatterns = [
    path('admin/', admin.site.urls),
]

flats = [
    path('api/flats/', FlatListView.as_view()),
    path('api/flats/<int:flat_pk>/', FlatDetailView.as_view()),
]

schema = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/schema/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='docs',
    ),
]

urlpatterns += flats + schema
