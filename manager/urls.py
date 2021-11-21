from django.urls import path
from . import views

from .views import (
    #GERENCIAMENTO DE DISCIPLINAS
    DisciplinaDetailView,
    DisciplinaCreateView,
    DisciplinaUpdateView,
    DisciplinaDeleteView,
    #GERENCIAMENTO DE AULAS
    AulaDetailView,
    AulaCreateView,
    AulaUpdateView,
    AulaDeleteView,
    #GERENCIAMENTO DE CURSOS
    CursoDetailView,
    CursoCreateView,
    CursoUpdateView,
    CursoDeleteView
)

urlpatterns = [
    #GERECIAMENTO DE DISCIPLINAS
    path('filtrarDisciplina/', views.filtrarDisciplina, name='filtrarDisciplina'),
    path('gerenciarDisciplina/', views.gerenciarDisciplina, name='gerenciarDisciplina'),
    path('disciplina/<int:pk>/', DisciplinaDetailView.as_view(), name='disciplina-detail'),
    path('disciplina/<int:pk>/delete/', DisciplinaDeleteView.as_view(), name='disciplina-delete'),
    path('disciplina/new/', DisciplinaCreateView.as_view(), name='disciplina-create'),
    path('disciplina/<int:pk>/update/', DisciplinaUpdateView.as_view(), name='disciplina-update'),

    #GERENCIAMENTO DE AULAS
    path('filtrarAula/', views.filtrarAula, name='filtrarAula'),
    path('gerenciarAula/', views.gerenciarAula, name='gerenciarAula'),
    path('aula/<int:pk>/', AulaDetailView.as_view(), name='aula-detail'),
    path('aula/<int:pk>/delete/', AulaDeleteView.as_view(), name='aula-delete'),
    path('aula/new/', AulaCreateView.as_view(), name='aula-create'),
    path('aula/<int:pk>/update/', AulaUpdateView.as_view(), name='aula-update'),

    #GERENCIAMENTO DE CURSOS
    path('gerenciarCurso/', views.gerenciarCurso, name='gerenciarCurso'),
    path('curso/<int:pk>/', CursoDetailView.as_view(), name='curso-detail'),
    path('curso/<int:pk>/delete/', CursoDeleteView.as_view(), name='curso-delete'),
    path('curso/new/', CursoCreateView.as_view(), name='curso-create'),
    path('curso/<int:pk>/update/', CursoUpdateView.as_view(), name='curso-update'),
]