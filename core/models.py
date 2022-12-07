from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

class Tipo(models.Model):
    nome = models.CharField('Nome', max_length=100, default='', null=True)

class Disciplina(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Area(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Usuario(AbstractUser):
    nome = models.CharField('Nome completo', max_length=100)
    matricula = models.CharField('Matrícula', max_length=14, primary_key=True, unique=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, default='', null=True)

    USERNAME_FIELD = 'matricula'

class Subarea(models.Model):
    nome = models.CharField('Nome', max_length=100)
    id_area = models.ForeignKey(Area, on_delete=models.PROTECT)

class Livro(models.Model):
    titulo = models.CharField('Título', max_length=100)
    autores = models.CharField('Autor(es)', max_length=200)
    data_lancamento = models.DateField('Data de lançamento')
    isbn = models.CharField('ISBN', max_length=13, primary_key=True)
    sinopse = models.CharField('Sinopse', max_length=5000)
    capa = models.ImageField(upload_to='static/imagem/', null='true')
    id_subarea = models.ForeignKey(Subarea, on_delete=models.PROTECT)

class Avaliacao(models.Model):
    nota_geral = models.IntegerField('Nota Geral')
    sinopse = models.CharField('Sinopse', max_length=5000)
    isbn_livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Recomendacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    isbn_livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
