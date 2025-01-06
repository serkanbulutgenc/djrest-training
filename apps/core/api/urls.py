from django.urls import path 
from rest_framework.routers import DefaultRouter

from apps.catalogue.api.views import (product_list,
                                       ProductListView, 
                                       ProductDetailView,
                                         ProductListCreateView,
                                           ProductDetailUpdateDestroyView,
                                             ProductListCreateAPIView,
                                             ProductDetailUpdateDestroyAPIView,
                                             ProductViewSet)

app_name = 'api-root'
router = DefaultRouter() 
router.register('products', ProductViewSet, basename='products')

urlpatterns = router.urls
