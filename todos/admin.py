# todos/admin.py
from django.contrib import admin
from .models import Estacao, Material, Produto, Veiculo

admin.site.register(Estacao)
admin.site.register(Material)
admin.site.register(Produto)
admin.site.register(Veiculo)


# Register your models here.
