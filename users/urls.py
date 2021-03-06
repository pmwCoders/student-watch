from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as user_views

from users.views import (
    LoginView
)


urlpatterns = [
    path('registrarPresenca/', user_views.registrarPresenca, name='registrarPresenca'),
    path('filtrarPresenca/', user_views.filtrarPresenca, name='filtrarPresenca'),
    path('visualizarPresenca/', user_views.visualizarPresenca, name='visualizarPresenca'),
    path('cadastrarProfessor/', user_views.professor_profile_view, name='cadastrarProfessor'),
    path('cadastrarEstudante/', user_views.estudante_profile_view, name='cadastrarEstudante'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('ajax/load-disciplinas/', user_views.load_disciplinas, name='ajax_load_disciplinas'),
    path('ajax/load-turnos/', user_views.load_turnos, name='ajax_load_turnos'),
]
