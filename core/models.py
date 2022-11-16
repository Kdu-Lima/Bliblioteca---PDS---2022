from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField('Nome completo', max_length=100)
    matricula = models.IntegerField('Matrícula', unique=True)
    administrador = models.BooleanField()

    USERNAME_FIELD: 'matricula'