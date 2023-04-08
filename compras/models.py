from django.db import models
from django.utils import timezone
from productos.models import Preparacion
from local.models import Totem

#comando salvador: manage.py migrate --run-syncdb
# Modelos de bloque Compras
# bloque productos = Cupon, Compra, Item compra

class Cupon(models.Model):
    nombre_cup = models.CharField(primary_key=True, max_length=32,null=False, blank=False, default='Ingresar nombre cupon', verbose_name='Nombre cupon')
    #id_cup = models.AutoField(null=False, blank=False, verbose_name='ID Cupon')
    desc_cup = models.IntegerField(verbose_name='Valor del descuento aplicado', default=0)
    fecha_inicio_cup = models.DateField(verbose_name='Fecha de inicio del cupon', default=timezone.now)
    fecha_fin_cup = models.DateField(verbose_name='Fecha de término del cupon', default=timezone.now)
    porc_desc_cup = models.IntegerField(verbose_name='Porcentaje de descuento %', default=0)
    stock_cup = models.IntegerField(verbose_name='Cantidad de cupones disponibles', default=0)
    id_compra = models.ForeignKey('Compra', on_delete=models.CASCADE, default='null', related_name='id_compra_cupon')
    
    class Meta:
        verbose_name='Cupon'
        verbose_name_plural='Cupones'
        ordering=['nombre_cup']

    def __str__(self):
        return self.nombre_cup

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID Compra')
    tipo_servicio_compra = models.CharField(max_length=32,null=False, blank=False, default='Para servir', verbose_name='Para servir o llevar')
    fecha_compra = models.DateTimeField(auto_now_add=True)
    estado_compra = models.CharField(max_length=32,null=False, blank=False, default='esperando', verbose_name='Estado compra')
    total_compra = models.IntegerField(verbose_name='Total de la compra', default=0)
    #nboleta_compra = models.AutoField(verbose_name='N boleta servicios de pago', default=0)
    procesador_pago_compra = models.CharField(max_length=15,null=False, blank=False, default='transbank', verbose_name='Tipo de pago')
    #campos medios de pago-------
    id_transaccion_compra = models.CharField(max_length=30, null=True, blank=False, default='0', verbose_name='ID Transaccion')
    cod_comercio_compra = models.CharField(max_length=15,null=True, blank=False, default='0', verbose_name='Cod comercio')
    respuesta_tb_compra = models.CharField(max_length=15,null=True, blank=False, default='0', verbose_name='Cod comercio')
    respuesta_mp_compra = models.CharField(max_length=15,null=True, blank=False, default='0', verbose_name='Cod comercio')
    totem_compra = models.ForeignKey(Totem, on_delete=models.PROTECT, default='null', related_name='id_totem_compra')

    class Meta:
        verbose_name='Compra'
        verbose_name_plural='Compras'
        ordering=['id_compra']

    def __int__(self):
        return self.id_compra

class Item_compra(models.Model):
    id_prep = models.ForeignKey(Preparacion, on_delete=models.CASCADE, default='null', related_name='id_prep_itemcompra')
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE, default='null', related_name='id_compra_itemcompra')
    cantidad_item = models.IntegerField(verbose_name='Cantidad del item', default=999)
    precio_unitario_item = models.IntegerField(verbose_name='Precio unitario item', default=999)
    total_item = models.IntegerField(verbose_name='Precio unitario item', default=0)

    class Meta:
        verbose_name='Item_compra'
        verbose_name_plural='Items_compra'
        ordering=['id_prep']

    def __int__(self):
        return self.id_prep