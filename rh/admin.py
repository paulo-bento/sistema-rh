from django.contrib import admin

from .models import Departamento, Funcionario, RegistroHoras

admin.site.register(Departamento)
admin.site.register(Funcionario)


@admin.register(RegistroHoras)
class RegistroHorasAdmin(admin.ModelAdmin):
    readonly_fields = ["horas_extras"]
