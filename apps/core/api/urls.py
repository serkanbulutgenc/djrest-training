from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.blog.api.views import CategoryViewSet, PostsViewSet
from apps.catalogue.api.views import (
    ProductDetailUpdateDestroyAPIView,
    ProductDetailUpdateDestroyView,
    ProductDetailView,
    ProductListCreateAPIView,
    ProductListCreateView,
    ProductListView,
    ProductViewSet,
    product_list,
)

app_name = "api-root"
router = DefaultRouter()
router.register("products", ProductViewSet, basename="product")
router.register("posts", PostsViewSet, basename="post")
router.register("categories", CategoryViewSet, basename="category")

urlpatterns = []

urlpatterns += router.urls
