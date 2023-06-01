from django.db import models
from django.core.exceptions import ValidationError
#comando salvador: python manage.py migrate --run-syncdb
# Modelos de bloque productos
# bloque productos = preparacion, detalle_preparacion, ingrediente, categoria

class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID Categoria')
    nombre_cat = models.CharField(null=False, blank=False, max_length=30, verbose_name='Nombre categoria')
    estado = models.BooleanField(null=False, blank=False, default=True, verbose_name='Estado categoria')

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['nombre_cat']
    
    # def clean(self):
    #     # Verificar si ya existe una categoría con el mismo nombre, ignorando mayúsculas y minúsculas
    #     categoria_existente = Categoria.objects.filter(nombre_cat__iexact=self.nombre_cat)
    #     if self.pk:
    #         categoria_existente = categoria_existente.exclude(pk=self.pk)
    #     if categoria_existente.exists():
    #         raise ValidationError('Ya existe una categoría con este nombre.'

    def __str__(self):
        return self.nombre_cat

class Ingrediente(models.Model):
    id_ingre = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID Ingrediente')
    nombre_ingre = models.CharField(max_length=55, default='Ingresar nombre', verbose_name='Nombre ingrediente')
    stock_ingrediente = models.IntegerField(verbose_name='stock ingrediente', default=0)
    tipo_unidad_ingrediente = models.CharField(max_length=32,null=False, blank=False, default='Ingresar tipo, gr o ml', verbose_name='Tipo unidad ingrediente')
    fecha_creacion_ingre = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion_ingre = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(null=False, blank=False, default=True, verbose_name='Estado ingrediente')
    # marca_ingre = models.CharField(max_length=32,null=False, blank=False, default='Ingresar marca', verbose_name='Marca')
    # cantidad_por_unidad_ingrediente = models.IntegerField(verbose_name='Cantidad de ingrediente por unidad', default=0)
    # imagen_ingre = models.CharField(max_length=300, default='Ingresar link imagen', verbose_name='Link imagen ingrediente')

    class Meta:
        verbose_name='Ingrediente'
        verbose_name_plural='Ingredientes'
        ordering=['nombre_ingre']

    def __int__(self):
        return self.id_ingre
    
class Detalle_preparacion(models.Model):
    id_detalle_prep = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID Detalle-prep')
    id_prep = models.ForeignKey('preparacion', on_delete=models.CASCADE, default='Blank', related_name='id_preparacion')
    id_ingre = models.ForeignKey('ingrediente', on_delete=models.CASCADE, default='Blank', related_name='id_ingrediente')
    cantidad_necesaria = models.IntegerField(verbose_name='Cantidad necesaria', null=False, default=1)
    tipo_unidad = models.CharField(max_length=10,null=False, default='Ingresar tipo unidad', verbose_name='Tipo unidad')
    estado = models.BooleanField(null=False, blank=False, default=True, verbose_name='Estado Detalle preparacion')

    class Meta:
        verbose_name='Detalle_prep'
        verbose_name_plural='Detalle_prep'
        ordering=['id_detalle_prep']

    def __int__(self):
        return self.id_detalle_prep
    
class Preparacion(models.Model):
    id_prep = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID Preparacion')
    nombre_prep = models.CharField(max_length=32,null=False, blank=False, default='Ingresar nombre', verbose_name='Nombre preparacion')
    descripcion_prep = models.CharField(max_length=300,null=False, blank=False, default='Ingresar descripcion', verbose_name='Descripcion preparacion')
    imagen_prep = models.CharField(max_length=300, default='Ingresar link imagen', verbose_name='Link imagen preparacion')
    id_cat_prep = models.ForeignKey('categoria', on_delete=models.CASCADE, default='Blank', related_name='id_categoria')
    precio_prep = models.IntegerField(null=False, default=0, verbose_name='Precio preparacion')
    estado = models.BooleanField(null=False, blank=False, default=True, verbose_name='Estado ingrediente')

    class Meta:
        verbose_name='Preparacion'
        verbose_name_plural='Preparacion'
        ordering=['nombre_prep']

    def __int__(self):
        return self.id_prep