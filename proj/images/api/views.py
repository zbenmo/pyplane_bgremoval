from http.client import HTTPResponse
from wsgiref.util import FileWrapper
from rest_framework import viewsets
from .serializers import ImageSerializer
from ..models import Image
from rest_framework.decorators import action

class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # /api/images/
    # /api/images/<pk>

    # /api/images/<pk>/download
    @action(methods=['GET'], detail=True)
    def download(self, *args, **kwargs):
        instance = self.get_object()
        img_path = instance.rmbg_img
        img = open(img_path, 'rb')
        response = HTTPResponse(FileWrapper(img), content_type='image/png')
        return response