from django.contrib import admin
from django.utils.text import slugify

from apps.blog.models import Category, Post, Tag

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "status", "created_at"]
    list_display_links = ["title"]
    list_per_page = 20
    list_filter = ["category", "status"]
    search_fields = ["title", "status"]

    def save_model(self, request, obj, form, change):
        slug_field = form.cleaned_data.get("slug")

        obj.slug = slug_field if len(slug_field) > 0 else slugify(obj.title)

        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]

    def save_model(self, request, obj, form, change):
        slug_field = form.cleaned_data.get("slug")

        obj.slug = slug_field if len(slug_field) > 0 else slugify(obj.title)

        super().save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]

    def save_model(self, request, obj, form, change):
        slug_field = form.cleaned_data.get("slug")

        obj.slug = slug_field if len(slug_field) > 0 else slugify(obj.title)

        super().save_model(request, obj, form, change)
