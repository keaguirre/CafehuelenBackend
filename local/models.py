from django.db import models

#comando salvador: manage.py migrate --run-syncdb
# Modelos de bloque Compras
# bloque productos = Local, Totem, Supervisores_local, Proveedor


class Local(models.Model):
    id_local = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID_Local')
    nombre_local = models.CharField(max_length=30, default='null', verbose_name='Nombre local')
    fono_local = models.CharField(max_length=15, default='null', verbose_name='Fono local')
    direccion_local = models.CharField(max_length=15, default='null', verbose_name='Direccion_local')

    class Meta:
        verbose_name='Local'
        verbose_name_plural='Locales'
        ordering=['id_local']

    def __int__(self):
        return self.id_local

class Totem(models.Model):
    mac_totem = models.CharField(primary_key=True, max_length=50, default='null', verbose_name='Mac Totem')
    num_totem = models.IntegerField(verbose_name='ID Totem', default=0)
    local_asignado = models.ForeignKey(Local, on_delete=models.SET_DEFAULT, default='null', related_name='id_local_totem')

    class Meta:
        verbose_name='Totem'
        verbose_name_plural='Totems'
        ordering=['num_totem']

    def __int__(self):
        return self.num_totem
    
class Superv_local(models.Model):
    usuario = models.CharField(primary_key=True, max_length=50, default='null', verbose_name='Usuario')
    contrasena = models.CharField(max_length=50, default='null', verbose_name='Usuario')
    local_asignado = models.ForeignKey(Local, default='null',related_name='id_local_superv', on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name='Supervisor_local'
        verbose_name_plural='Supervisores_local'
        ordering=['local_asignado']

    def __str__(self):
        return self.usuario

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID proveedor')
    nombre_prove = models.CharField(max_length=50, default='null', verbose_name='Usuario')
    num_prove = models.CharField(max_length=50, default='null', verbose_name='Usuario')
    ingredientes_prove = models.CharField(max_length=50, default='null', verbose_name='Usuario')
#   id_local_prove = models.ForeignKey(related_name='local_id', on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'
        ordering=['nombre_prove']

    def __str__(self):
        return self.nombre_prove