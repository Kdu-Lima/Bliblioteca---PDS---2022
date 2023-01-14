from cProfile import label
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

class Tipo(models.Model):
    nome = models.CharField('Nome', max_length=100, default='', null=True)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome

class Area(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    nome = models.CharField('Nome completo', max_length=100)
    username = models.CharField('Matrícula', max_length=14, primary_key=True, unique=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, default='', null=True, verbose_name='Tipo')

    USERNAME_FIELD = 'username'

class Subarea(models.Model):
    nome = models.CharField('Nome', max_length=100)
    id_area = models.ForeignKey(Area, on_delete=models.PROTECT, verbose_name='Area')
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField('Título', max_length=100)
    autores = models.CharField('Autor(es)', max_length=200)
    data_lancamento = models.DateField('Data de lançamento')
    isbn = models.CharField('ISBN', max_length=13, primary_key=True)
    sinopse = models.CharField('Sinopse', max_length=5000)
    capa = models.ImageField(upload_to='media', null='true')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name='Usuário', null=True)
    id_subarea = models.ForeignKey(Subarea, on_delete=models.PROTECT, verbose_name='Subarea')

    def __str__(self):
        return self.titulo

class Recomendacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name='Usuário')
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, verbose_name='Disciplina')
    isbn_livro = models.ForeignKey(Livro, on_delete=models.PROTECT, verbose_name='Livro')

class Avaliacao(models.Model):
    nota_geral = models.IntegerField('Nota Geral') #Pesquisar como inserir valores pré-definidos
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name='Usuário')
    resenha = models.CharField('Resenha', max_length=5000, null=True)
    id_recomendacao = models.ForeignKey(Recomendacao, on_delete=models.PROTECT, verbose_name='Recomendação', null=True)