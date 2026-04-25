from django import forms

from .models import Funcionario, RegistroHoras


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            "user",
            "departamento",
            "cargo",
            "salario",
            "carga_horaria_semanal",
            "data_admissao",
        ]
        widgets = {
            "data_admissao": forms.DateInput(attrs={"type": "date"}),
        }


class RegistroHorasForm(forms.ModelForm):
    class Meta:
        model = RegistroHoras
        fields = ["funcionario", "data", "horas_trabalhadas", "observacao"]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}),
        }
