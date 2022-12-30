from django.contrib import admin
from django.urls import path
from core.views import teste, T_inicial, registro, base, aut, perfil, cadastro_manual
from django.contrib.auth.views import LoginView, LogoutView

#Para os cruds:-------------------------------------------------------------------------------------------------------------------------------
from core.views import listar_area, listar_avaliacao, listar_disciplina, listar_recomendacao, listar_subarea, listar_tipo
from core.views import cadastrar_area, cadastrar_avaliacao, cadastrar_disciplina, cadastrar_recomendacao, cadastrar_subarea, cadastrar_tipo
from core.views import editar_area, editar_avaliacao, editar_disciplina, editar_recomendacao, editar_subarea, editar_tipo
from core.views import remover_area, remover_avaliacao, remover_disciplina, remover_recomendacao, remover_subarea, remover_tipo
#---------------------------------------------------------------------------------------------------------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', teste ),
    path('', T_inicial, name='inicial'),
    path('registro/', registro),
    path('base/', base),
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('perfil/', perfil, name='perfil'),
    path('cadastro_manual/', cadastro_manual),

    #Cruds:----------------------------------------------------------------------------------------------------------------------------------
    path('area/', listar_area, name='listar_area'),
    path('avaliacao/', listar_avaliacao, name='listar_avaliacao'),
    path('disciplina/', listar_disciplina, name='listar_disciplina'),
    path('recomendacao/', listar_recomendacao, name='listar_recomendacao'),
    path('subarea/', listar_subarea, name='listar_subarea'),
    path('tipo/', listar_tipo, name='listar_tipo'),




    path('area_cadastrar/', cadastrar_area, name='cadastrar_area'),
    path('avaliacao_cadastrar/', cadastrar_avaliacao, name='cadastrar_avaliacao'),
    path('disciplina_cadastrar/', cadastrar_disciplina, name='cadastrar_disciplina'),
    path('recomendacao_cadastrar/', cadastrar_recomendacao, name='cadastrar_recomendacao'),
    path('subarea_cadastrar/', cadastrar_subarea, name='cadastrar_subarea'),
    path('tipo_cadastrar/', cadastrar_tipo, name='cadastrar_tipo'),





    path('area_editar/<int:id>', editar_area, name='editar_area'),
    path('avaliacao_editar/<int:id>', editar_avaliacao, name='editar_avaliacao'),
    path('disciplina_editar/<int:id>', editar_disciplina, name='editar_disciplina'),
    path('recomendacao_editar/<int:id>', editar_recomendacao, name='editar_recomendacao'),
    path('subarea_editar/<int:id>', editar_subarea, name='editar_subarea'),
    path('tipo_editar/<int:id>', editar_tipo, name='editar_tipo'),





    path('area_remover/<int:id>', remover_area, name='remover_area'),
    path('avaliacao_remover/<int:id>', remover_avaliacao, name='remover_avaliacao'),
    path('disciplina_remover/<int:id>', remover_disciplina, name='remover_disciplina'),
    path('recomendacao_remover/<int:id>', remover_recomendacao, name='remover_recomendacao'),
    path('subarea_remover/<int:id>', remover_subarea, name='remover_subarea'),
    path('tipo_remover/<int:id>', remover_tipo, name='remover_tipo'),
    #-------------------------------------------------------------------------------------------------------------------------------------------
]
