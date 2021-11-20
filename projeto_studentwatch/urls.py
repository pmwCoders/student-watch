"""projeto_studentwatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from manager import views as manager_views

from users.views import (
    LoginView
)

from manager.views import (
    DisciplinaDetailView,
    DisciplinaCreateView,
    DisciplinaUpdateView,
    DisciplinaDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrarCurso/', manager_views.cadastrarCurso, name='cadastrarCurso'),
    path('registrarPresenca/', user_views.registrarPresenca, name='registrarPresenca'),
    path('filtrarPresenca/', user_views.filtrarPresenca, name='filtrarPresenca'),
    path('visualizarPresenca/', user_views.visualizarPresenca, name='visualizarPresenca'),
    path('filtrarDisciplina/', manager_views.filtrarDisciplina, name='filtrarDisciplina'),
    path('gerenciarDisciplina/', manager_views.gerenciarDisciplina, name='gerenciarDisciplina'),
    path('disciplina/<int:pk>/', DisciplinaDetailView.as_view(), name='disciplina-detail'),
    path('disciplina/<int:pk>/delete/', DisciplinaDeleteView.as_view(), name='disciplina-delete'),
    path('disciplina/new/', DisciplinaCreateView.as_view(), name='disciplina-create'),
    path('disciplina/<int:pk>/update/', DisciplinaUpdateView.as_view(), name='disciplina-update'),
    path('cadastrarProfessor/', user_views.professor_profile_view, name='cadastrarProfessor'),
    path('cadastrarEstudante/', user_views.estudante_profile_view, name='cadastrarEstudante'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('page.urls')),

    path('ajax/load-disciplinas/', manager_views.load_disciplinas, name='ajax_load_disciplinas'),
]

handler403 = 'users.views.error_403_view'