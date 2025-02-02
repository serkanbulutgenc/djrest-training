from django.utils.timezone import now
from rest_framework import serializers

from apps.blog.models import Category, Post, get_user_model


class CategorySerializer(serializers.ModelSerializer):

    # category = serializers.HyperlinkedIdentityField()
    class Meta:
        model = Category
        fields = "__all__"


class PostSummarySerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    # owner = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "summary",
            "category",
            "owner",
            "tags",
            "published_at",
        )


class PostSerializer(PostSummarySerializer):
    # category = serializers.StringRelatedField(many=False)
    # category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='title')
    tags = serializers.StringRelatedField(many=True, read_only=True)
    owner = serializers.PrimaryKeyRelatedField(
        many=False, queryset=get_user_model().objects.all()
    )
    # days_since_joined = serializers.SerializerMethodField()

    def save(self, **kwargs):
        return super().save(**kwargs)

    class Meta(PostSummarySerializer.Meta):
        fields = "__all__"
        # exclude = ["created_at", "updated_at"]

    # def get_days_since_joined(self, obj):
    #    return (now() - obj.published_at).days
