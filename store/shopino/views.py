from django.shortcuts import render

from .models import Shop
from .serializers import ShopSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework import status

class ShopViewSet(viewsets.ModelViewSet):

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    # @action(detail=True, renderer_classes=[StaticHTMLRenderer])
    # # def highlight(self, request, *args, **kwargs):
    # #     shop = self.get_object()
    # #     return Response(shop.highlighted)
    #
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


