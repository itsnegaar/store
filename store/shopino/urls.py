from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShopViewSet, ProductViewSet, ShopsProductViewset, BookmarkView , BookmarkedUsersView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'shop', ShopViewSet, basename="shop")
router.register(r'product', ProductViewSet, basename="product")
router.register(r'shop/(?P<id>\d+)/product', ShopsProductViewset, basename="shops_product")



# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('product/<int:id>/bookmark/', BookmarkView.as_view(), name='bookmark'),
    path('product/<int:product_id>/bookmarked-users/', BookmarkedUsersView.as_view(), name='bookmarked-users'),
    path("__debug__/", include("debug_toolbar.urls")),

]
