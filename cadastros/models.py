from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    valor_divida = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='cadastros')

    def __str__(self):
        return self.nome