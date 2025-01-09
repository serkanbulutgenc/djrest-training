from django.urls import path
from .views import posts_view, PostsView, PostListCreateView, PostsViewSet




urlpatterns = [
    #path('posts/', posts_view, name='posts-lists')
    #path('posts/', PostsView.as_view(), name='posts-lists')
    #path('posts/', PostListCreateView.as_view(), name='posts-lists')
]
