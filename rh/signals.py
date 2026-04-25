from decimal import Decimal

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import RegistroHoras


@receiver(pre_save, sender=RegistroHoras)
def calcular_horas_extras(sender, instance, **kwargs):
    horas_diarias = Decimal(instance.funcionario.carga_horaria_semanal) / Decimal(5)
    extras = instance.horas_trabalhadas - horas_diarias
    instance.horas_extras = extras if extras > 0 else Decimal(0)
