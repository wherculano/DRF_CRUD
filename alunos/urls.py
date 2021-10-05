from django.urls import path
from alunos import views

urlpatterns = [
    path('getAluno/', views.AlunoList, name='listar'),
    path('postAluno/', views.AlunoPost, name='cadastrar'),
    path('putAluno/<str:pk>/', views.AlunoPut, name='atualizar'),
    path('delAluno/<str:pk>/', views.AlunoDelete, name='excluir')
]
