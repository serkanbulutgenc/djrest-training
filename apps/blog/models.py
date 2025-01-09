from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=75, help_text=_("Category title"))
    meta_title = models.CharField(
        _("Meta Title"),
        null=True,
        blank=True,
        max_length=100,
        help_text=_("Category meta title"),
    )
    slug = models.SlugField(
        _("Slug"), unique=True, blank=True, help_text=_("Category slug")
    )
    content = models.TextField(
        _("Content"), blank=True, null=True, help_text=_("Category content")
    )
    created_at = models.DateTimeField(
        _("Created at"), editable=False, auto_now_add=True, help_text=_("Created date")
    )
    updated_at = models.DateTimeField(
        _("Updated at"), editable=False, auto_now=True, help_text=_("Updated date")
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["title"]


class Tag(models.Model):
    title = models.CharField(_("Title"), max_length=50, help_text=_("Slug title"))
    meta_title = models.CharField(
        _("Meta Title"),
        null=True,
        blank=True,
        max_length=100,
        help_text=_("Tag meta title"),
    )
    slug = models.SlugField(_("Slug"), unique=True, blank=True, help_text=_("Tag slug"))
    created_at = models.DateTimeField(
        _("Created at"), editable=False, auto_now_add=True, help_text=_("Created date")
    )
    updated_at = models.DateTimeField(
        _("Updated at"), editable=False, auto_now=True, help_text=_("Updated date")
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["-created_at"]


class Comment(models.Model):
    pass


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "DRAFT"
        PENDING = "pending", "PENDING"
        PUBLISHED = "published", "PUBLISHED"

    title = models.CharField(_("Title"), max_length=75, help_text=_("Post title"))
    meta_title = models.CharField(
        _("Meta Title"),
        null=True,
        blank=True,
        max_length=100,
        help_text=_("Post meta title"),
    )
    slug = models.SlugField(_("Slug"), unique=True, blank=True, help_text=_("Post slug"))
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="posts",
        help_text=_("Post owner"),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        help_text=_("Post Category"),
        related_name="posts",
    )
    tags = models.ManyToManyField(
        Tag, related_name="posts", blank=True, help_text=_("Post tags")
    )
    likes = models.ManyToManyField(
        get_user_model(),
        blank=True,
        editable=False,
        related_name="liked_posts",
        help_text=_("Post like count"),
    )
    status = models.CharField(
        _("Status"),
        choices=Status.choices,
        default=Status.DRAFT,
        blank=True,
        max_length=15,
        help_text=_("Post status"),
    )
    summary = models.CharField(
        _("Summary"), blank=True, null=True, max_length=200, help_text=_("Post summary")
    )
    content = models.TextField(_("Content"), help_text=_("Post content"))
    created_at = models.DateTimeField(
        _("Created at"), editable=False, auto_now_add=True, help_text=_("Created date")
    )
    updated_at = models.DateTimeField(
        _("Updated at"), editable=False, auto_now=True, help_text=_("Updated date")
    )
    published_at = models.DateTimeField(
        _("Published at"), blank=True, null=True, help_text=_("Published date")
    )

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]
