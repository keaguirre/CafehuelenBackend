from django.contrib import admin
from .models import Categoria, Ingrediente, Detalle_preparacion, Preparacion

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Ingrediente)
admin.site.register(Detalle_preparacion)
admin.site.register(Preparacion)