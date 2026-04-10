from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    published_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to="images")
    author_name = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"
        ordering = ["-published_at"]

class Reserva(models.Model):
    nome_completo = models.CharField(max_length=200)
    data_horario = models.DateTimeField()
    quantidade_pessoas = models.IntegerField()

    def __str__(self):
        return f"{self.nome_completo} - {self.data_horario}"