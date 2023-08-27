from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shopino import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'shop', views.ShopViewSet,basename="shop")
router.register(r'product', views.ProductViewSet,basename="product")
router.register(r'shop/(?P<id>\d+)/product', views.ShopsProductViewset,basename="shops_product")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]