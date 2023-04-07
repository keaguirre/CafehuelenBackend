from django.contrib import admin
from .models import Cupon, Compra, Item_compra

# Register your models here.
admin.site.register(Cupon)
admin.site.register(Compra)
admin.site.register(Item_compra)