from django.db import models


# Create your models here.
class Reserva(models.Model):
    nome_completo = models.CharField(max_length=200)
    data_horario = models.DateTimeField()
    quantidade_pessoas = models.IntegerField()

    def __str__(self):
        return f"{self.nome_completo} - {self.data_horario}"


