from django.db import models

# Create your models here.
class Filmes(models.Model):
    nome = models.CharField(max_length=150)
    duracao= models.CharField(max_length=100)
    ano = models.IntegerField()
    produtor = models.CharField(max_length=100)
    diretor= models.CharField(max_length=100)
    elenco = models.CharField(max_length=100)
    direcao = models.CharField(max_length=100)