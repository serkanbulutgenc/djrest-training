import random
from collections import OrderedDict

import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.utils.timezone import get_current_timezone
from factory.django import DjangoModelFactory, mute_signals

from apps.blog.models import Category, Post, Tag

F = factory.faker.faker.Faker()


@mute_signals(post_save)
class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Faker("text")


@mute_signals(post_save)
class UserFactory(DjangoModelFactory):

    class Meta:
        model = get_user_model()

    username = factory.Faker("user_name")  # F.simple_profile().get("username")
    email = factory.Faker("email")  # F.simple_profile().get("mail")
    is_staff = True

    @factory.post_generation
    def password(obj, create, extracted, **kwargs):
        if not create:
            return
        # print("obj", obj, type(obj))
        obj.set_password("7745283")


@mute_signals(post_save)
class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post
        django_get_or_create = ("title",)

    title = factory.Faker("sentence", nb_words=6, variable_nb_words=True)
    meta_title = factory.Faker("text", max_nb_chars=100)
    status = factory.Faker(
        "random_element",
        elements=OrderedDict([("draft", 0.3), ("pending", 0.2), ("published", 0.5)]),
    )
    # owner=factory.Iterator()
    summary = factory.Faker("sentence", nb_words=14, variable_nb_words=True)
    category = factory.Iterator(Category.objects.all())
    # category = factory.SubFactory(CategoryFactory)
    published_at = factory.Faker(
        "date_time_between", start_date="-1y", tzinfo=get_current_timezone()
    )

    @factory.lazy_attribute
    def slug(self):
        return slugify(self.title)

    @factory.lazy_attribute
    def content(self):
        return "\n".join(F.paragraphs(nb=3))

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        # TODO

        selected_tags = random.choices(extracted, k=3)

        self.tags.add(*selected_tags)


@mute_signals(post_save)
class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ("title",)

    title = factory.LazyAttribute(lambda o: " ".join(F.words(nb=1, unique=True)))
    meta_title = factory.Faker("text", max_nb_chars=100)
    posts = factory.RelatedFactoryList(
        PostFactory, factory_related_name="category", size=lambda: random.randint(5, 30)
    )

    @factory.lazy_attribute
    def slug(self):
        return slugify(self.title)

    @factory.lazy_attribute
    def content(self):
        return "\n".join(F.paragraphs(nb=3))


@mute_signals(post_save)
class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag
        django_get_or_create = ("title",)

    title = factory.Faker("word")
    meta_title = factory.Faker("text", max_nb_chars=100)

    @factory.lazy_attribute
    def slug(self):
        return slugify(self.title)
