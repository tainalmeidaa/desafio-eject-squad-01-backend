from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from blog.models import Post


@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    list_display = ("id", "title", "author_name", "published_at", "cover")
    list_display_links = ("title",)
    list_filter = ("published_at", "author_name")
    search_fields = ("title", "author_name", "excerpt", "content")
    ordering = ("-published_at",)
    readonly_fields = ("id", "published_at")
    fields = (
        "id",
        "title",
        "excerpt",
        "cover",
        "author_name",
        "content",
        "published_at",
    )
