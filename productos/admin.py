from django.contrib import admin
from .models import categoria, ingrediente, detalle_preparacion, preparacion

# Register your models here.
admin.site.register(categoria)
admin.site.register(ingrediente)
admin.site.register(detalle_preparacion)
admin.site.register(preparacion)