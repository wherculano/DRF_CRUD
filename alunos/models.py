from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=14)
