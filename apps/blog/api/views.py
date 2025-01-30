# from http import HTTPMethod

from django.shortcuts import get_list_or_404
from django.utils.text import slugify
from rest_framework import generics, mixins, permissions, status
from rest_framework.decorators import action, api_view
from rest_framework.permissions import (
    BasePermission,
    DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.blog.api.serializers import (
    CategorySerializer,
    PostSerializer,
    PostSummarySerializer,
)
from apps.blog.models import Category, Post


@api_view(["GET"])
def posts_view(request):
    posts = get_list_or_404(Post)
    serializer = PostSerializer(posts, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostsView(APIView):
    def get(self, request, format=None):
        posts = get_list_or_404(Post)
        serializer = PostSerializer(posts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostListCreateView(mixins.ListModelMixin, generics.GenericAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()[:2]

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset()
        return Post.objects.filter(owner=user)

    def get_serializer_class(self):
        if self.action == "list":
            return PostSummarySerializer
        else:
            return PostSerializer

    def perform_create(self, serializer):
        serializer.validated_data["slug"] = slugify(serializer.validated_data["title"])
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=["GET"])
    def recent(self, request):
        recent_posts = Post.objects.order_by("-published_at")[:2]
        serializer = PostSerializer(recent_posts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
