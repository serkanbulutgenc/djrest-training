import random
from itertools import cycle

from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from apps.blog.factories import (
    CategoryFactory,
    GroupFactory,
    PostFactory,
    TagFactory,
    UserFactory,
)
from apps.blog.models import Post


class Command(BaseCommand):
    help = "Inserts the post, category and tag to the blog database with given count."

    def add_arguments(self, parser):
        parser.add_argument(
            "-p", "--post-count", nargs="?", default=30, type=int, help="Post count"
        )
        parser.add_argument(
            "-t", "--tag-count", nargs="?", default=15, type=int, help="Tag count"
        )
        parser.add_argument(
            "-c",
            "--category-count",
            nargs="?",
            default=10,
            type=int,
            help="Category count",
        )

    def handle(self, *args, **options):
        GROUPS = ("author", "editor", "manager")
        post_count = options.get("post_count")
        tag_count = options.get("tag_count")
        category_count = options.get("category_count")

        if post_count < 0 or tag_count < 0 or category_count < 0:
            raise ValueError(f"Count value must be greater than zero")

        categories = CategoryFactory.create_batch(category_count)

        print(f"Total {len(categories)} categories have been created.")

        for group in GROUPS:
            try:
                Group.objects.get(name=group)
            except Group.DoesNotExist as ex:
                GroupFactory.create(name=group)

        print(f"{len(GROUPS)} groups have been created.")

        users = UserFactory.create_batch(10)

        print(f"{len(users)} users have been created.")

        tags = TagFactory.create_batch(tag_count)

        user_cycle = cycle(users)

        print(f"{len(tags)} tags have been created.")

        posts = Post.objects.all()

        for post in posts:
            post.owner = next(user_cycle)
            post.tags.add(*random.choices(tags, k=3))

        Post.objects.bulk_update(posts, ["owner"])
