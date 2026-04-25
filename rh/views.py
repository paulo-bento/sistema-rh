from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import FuncionarioForm, RegistroHorasForm
from .models import Funcionario, RegistroHoras


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "rh/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            ctx["total_funcionarios"] = Funcionario.objects.count()
            ctx["funcionarios_recentes"] = Funcionario.objects.order_by(
                "-data_admissao"
            )[:5]
        else:
            try:
                ctx["funcionario"] = self.request.user.funcionario
                ctx["registros_recentes"] = (
                    self.request.user.funcionario.registros.all()[:5]
                )
            except Funcionario.DoesNotExist:
                pass
        return ctx


# Funcionario 


class FuncionarioListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Funcionario
    template_name = "rh/funcionario_list.html"
    context_object_name = "funcionarios"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(user__first_name__icontains=q) | qs.filter(
                user__last_name__icontains=q
            )
        return qs


class FuncionarioDetailView(LoginRequiredMixin, DetailView):
    model = Funcionario
    template_name = "rh/funcionario_detail.html"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Funcionario.objects.all()
        return Funcionario.objects.filter(user=self.request.user)


class FuncionarioCreateView(
    LoginRequiredMixin, AdminRequiredMixin, SuccessMessageMixin, CreateView
):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = "rh/funcionario_form.html"
    success_url = reverse_lazy("funcionario_list")
    success_message = "Funcionário cadastrado com sucesso."


class FuncionarioUpdateView(
    LoginRequiredMixin, AdminRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = "rh/funcionario_form.html"
    success_url = reverse_lazy("funcionario_list")
    success_message = "Funcionário atualizado com sucesso."


class FuncionarioDeleteView(
    LoginRequiredMixin, AdminRequiredMixin, SuccessMessageMixin, DeleteView
):
    model = Funcionario
    template_name = "rh/funcionario_confirm_delete.html"
    success_url = reverse_lazy("funcionario_list")
    success_message = "Funcionário removido com sucesso."


# egistroHoras


class RegistroHorasListView(LoginRequiredMixin, ListView):
    model = RegistroHoras
    template_name = "rh/registro_list.html"
    context_object_name = "registros"
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_staff:
            return RegistroHoras.objects.select_related("funcionario__user").all()
        return RegistroHoras.objects.filter(funcionario__user=self.request.user)


class RegistroHorasCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = RegistroHoras
    form_class = RegistroHorasForm
    template_name = "rh/registro_form.html"
    success_url = reverse_lazy("registro_list")
    success_message = "Registro adicionado com sucesso."


class RegistroHorasUpdateView(
    LoginRequiredMixin, AdminRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = RegistroHoras
    form_class = RegistroHorasForm
    template_name = "rh/registro_form.html"
    success_url = reverse_lazy("registro_list")
    success_message = "Registro atualizado com sucesso."


class RegistroHorasDeleteView(
    LoginRequiredMixin, AdminRequiredMixin, SuccessMessageMixin, DeleteView
):
    model = RegistroHoras
    template_name = "rh/registro_confirm_delete.html"
    success_url = reverse_lazy("registro_list")
    success_message = "Registro removido com sucesso."
