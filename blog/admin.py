from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author_name", "published_at", "cover")
    list_display_links = ("title",)
    list_filter = ("published_at", "author_name")
    search_fields = ("title", "author_name", "excerpt", "content")
    ordering = ("-published_at",)
    readonly_fields = ("published_at",)
    fields = ("title", "excerpt", "cover", "author_name", "content", "published_at")
