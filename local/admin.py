from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Local, Totem, Superv_local

# Register your models here.
admin.site.register(Local)
admin.site.register(Totem)
admin.site.register(Superv_local)
