from django.contrib.auth.models import User
from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    CARGO_CHOICES = [
        ("gerente", "Gerente"),
        ("assistente", "Assistente"),
        ("diretor", "Diretor"),
        ("estagiario", "Estagiário"),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="funcionario"
    )
    departamento = models.ForeignKey(
        Departamento, on_delete=models.SET_NULL, null=True, related_name="funcionarios"
    )
    cargo = models.CharField(max_length=50, choices=CARGO_CHOICES)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    carga_horaria_semanal = models.PositiveIntegerField(default=40)
    data_admissao = models.DateField()

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ["user__first_name"]

    def __str__(self):
        return f"{self.user.get_full_name()} — {self.get_cargo_display()}"


class RegistroHoras(models.Model):
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.CASCADE, related_name="registros"
    )
    data = models.DateField()
    horas_trabalhadas = models.DecimalField(max_digits=5, decimal_places=2)
    horas_extras = models.DecimalField(
        max_digits=5, decimal_places=2, default=0, editable=False
    )
    observacao = models.TextField(blank=True)

    class Meta:
        verbose_name = "Registro de Horas"
        verbose_name_plural = "Registros de Horas"
        ordering = ["-data"]

    def __str__(self):
        return f"{self.funcionario} — {self.data}"
