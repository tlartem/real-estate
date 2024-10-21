from django.contrib import admin
from django.urls import include, path
from realty.views import FlatView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'flats', FlatView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
