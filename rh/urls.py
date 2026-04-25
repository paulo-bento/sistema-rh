from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="rh/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # Funcionarios
    path("funcionarios/", views.FuncionarioListView.as_view(), name="funcionario_list"),
    path(
        "funcionarios/novo/",
        views.FuncionarioCreateView.as_view(),
        name="funcionario_create",
    ),
    path(
        "funcionarios/<int:pk>/",
        views.FuncionarioDetailView.as_view(),
        name="funcionario_detail",
    ),
    path(
        "funcionarios/<int:pk>/editar/",
        views.FuncionarioUpdateView.as_view(),
        name="funcionario_update",
    ),
    path(
        "funcionarios/<int:pk>/excluir/",
        views.FuncionarioDeleteView.as_view(),
        name="funcionario_delete",
    ),
    # Registros de Horas
    path("registros/", views.RegistroHorasListView.as_view(), name="registro_list"),
    path(
        "registros/novo/",
        views.RegistroHorasCreateView.as_view(),
        name="registro_create",
    ),
    path(
        "registros/<int:pk>/editar/",
        views.RegistroHorasUpdateView.as_view(),
        name="registro_update",
    ),
    path(
        "registros/<int:pk>/excluir/",
        views.RegistroHorasDeleteView.as_view(),
        name="registro_delete",
    ),
]
