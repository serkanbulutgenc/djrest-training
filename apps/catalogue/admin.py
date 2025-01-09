from django.contrib import admin
from apps.catalogue.models import Product, Comment
from django.utils.text import slugify
# Register your models here.

class CommentInline(admin.TabularInline):
    fields=('body',)
    model = Comment
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']


    def save_model(self, request, obj, form, change):

        obj.slug = form.cleaned_data.get('slug') if form.cleaned_data['slug'] else slugify(form.cleaned_data['title'])

        return super().save_model(request, obj, form, change)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','created_at']
