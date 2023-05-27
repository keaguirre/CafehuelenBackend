from django.db import models

#comando salvador: python manage.py migrate --run-syncdb
# Modelos de bloque Compras
# bloque productos = Local, Totem, Supervisores_local


class Local(models.Model):
    id_local = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID_Local')
    nombre_local = models.CharField(max_length=30, default='null', verbose_name='Nombre local')
    fono_local = models.CharField(max_length=32, default='null', verbose_name='Fono local')
    direccion_local = models.CharField(max_length=100, default='null', verbose_name='Direccion_local')
    estado = models.BooleanField(null=False, blank=False, default=True, verbose_name='Estado Local')
    class Meta:
        verbose_name='Local'
        verbose_name_plural='Locales'
        ordering=['id_local']

    def __int__(self):
        return self.id_local
    
class Superv_local(models.Model):
    usuario = models.CharField(primary_key=True, max_length=50, default='null', verbose_name='Usuario')
    contrasena = models.CharField(max_length=256, default='null', verbose_name='Contrasena')
    local_asignado = models.ForeignKey(Local,related_name='id_local_superv', on_delete=models.CASCADE)
    estado = models.BooleanField(null=False, blank=False, default=True, verbose_name='Estado Supervisor')

    class Meta:
        verbose_name='Supervisor_local'
        verbose_name_plural='Supervisores_local'
        ordering=['local_asignado']

    def __str__(self):
        return self.usuario

# class Totem(models.Model):
#     num_totem = models.AutoField(primary_key=True, verbose_name='ID Totem')
#     mac_totem = models.CharField(max_length=50, default='null', verbose_name='Mac Totem')
#     local_asignado = models.ForeignKey(Local, on_delete=models.CASCADE, default='null', related_name='id_local_totem')
#     estado = models.BooleanField(null=False, blank=False, default=True, verbose_name='Estado Totem')

#     class Meta:
#         verbose_name='Totem'
#         verbose_name_plural='Totems'
#         ordering=['num_totem']

#     def __int__(self):
#         return self.num_totem