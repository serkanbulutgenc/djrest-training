from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.blog.models import Post, Category, Tag

@receiver(post_save, sender=Post)
def post_saved(sender,instance, **kwargs):
    print(f'Post saved: {instance}')

@receiver(post_save, sender=Category)
def category_saved(sender,instance, **kwargs):
    print(f'Category saved: {instance}')

@receiver(post_save, sender=Tag)
def tag_saved(sender,instance, **kwargs):
    print(f'Tag saved: {instance}')