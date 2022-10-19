from images.api.views import ImageViewset
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'images', ImageViewset)

urlpatterns = [
    path('', include(router.urls))
]