from django.db import models
from markdownx.models import MarkdownxField


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    published_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to="images")
    author_name = models.CharField(max_length=50)
    content = MarkdownxField()

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"
        ordering = ["-published_at"]
