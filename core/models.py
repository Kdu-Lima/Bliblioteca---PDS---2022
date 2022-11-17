from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

class Tipo(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Usuario(AbstractUser):
    nome = models.CharField('Nome completo', max_length=100)
    matricula = models.CharField('Matrícula', max_length=14, unique=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)

    USERNAME_FIELD: 'matricula'