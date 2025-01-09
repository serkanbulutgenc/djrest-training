from django.urls import path , include
from rest_framework.routers import DefaultRouter
from apps.blog.api.urls import posts_view

from apps.catalogue.api.views import (product_list,
                                       ProductListView, 
                                       ProductDetailView,
                                         ProductListCreateView,
                                           ProductDetailUpdateDestroyView,
                                             ProductListCreateAPIView,
                                             ProductDetailUpdateDestroyAPIView,
                                             ProductViewSet)
from apps.blog.api.views import PostsViewSet

app_name = 'api-root'
router = DefaultRouter() 
router.register('products', ProductViewSet, basename='product')
router.register('posts', PostsViewSet, basename='post')

urlpatterns = [
    path('', include('apps.blog.api.urls') )
]

urlpatterns += router.urls
