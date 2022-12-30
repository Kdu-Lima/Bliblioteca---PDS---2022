from dataclasses import field, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

#Para os cruds:------------------------------------------------------------------------------------------------------------------------------
from django.forms import ModelForm
from .models import Area, Avaliacao, Disciplina, Recomendacao, Subarea, Tipo


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','password1','password2','email','tipo','nome']





#Para os cruds:------------------------------------------------------------------------------------------------------------------------------
class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['nome']

class AvaliacaoForm(ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota_geral', 'usuario', 'resenha', 'id_recomendacao']

class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome']

class RecomendacaoForm(ModelForm):
    class Meta:
        model = Recomendacao
        fields = ['usuario', 'id_disciplina', 'isbn_livro']

class SubareaForm(ModelForm):
    class Meta:
        model = Subarea
        fields = ['nome', 'id_area']

class TipoForm(ModelForm):
    class Meta:
        model = Tipo
        fields = ['nome']