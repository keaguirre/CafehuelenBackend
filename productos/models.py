from django.db import models
from django.core.exceptions import ValidationError
#comando salvador: python manage.py migrate --run-syncdb
# Modelos de bloque productos
# bloque productos = preparacion, ingredientes_preparacion, ingrediente, categoria

class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID Categoria')
    nombre_cat = models.CharField(null=False, blank=False, max_length=30, unique=True, verbose_name='Nombre categoria', 
                                  error_messages={'unique': 'Ya existe una categoría con este nombre.'})

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['nombre_cat']
    
    def clean(self):
        # Verificar si ya existe una categoría con el mismo nombre, ignorando mayúsculas y minúsculas
        existing_categories = Categoria.objects.filter(nombre_cat__iexact=self.nombre_cat)
        if self.pk:
            existing_categories = existing_categories.exclude(pk=self.pk)
        if existing_categories.exists():
            raise ValidationError('Ya existe una categoría con este nombre.')

    def __str__(self):
        return f"{self.id_cat} - {self.nombre_cat}"
        
class Ingrediente(models.Model):
    id_ingre = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID Ingrediente')
    marca_ingre = models.CharField(max_length=32,null=False, blank=False, default='Ingresar marca', verbose_name='Marca')
    descripcion_ingre = models.CharField(max_length=55, default='Ingresar descripcion', verbose_name='Descripcion')
    stock_ingrediente = models.IntegerField(verbose_name='stock ingrediente', default=0)
    cantidad_por_unidad_ingrediente = models.IntegerField(verbose_name='Cantidad de ingrediente por unidad', default=0)
    tipo_unidad_ingrediente = models.CharField(max_length=32,null=False, blank=False, default='Ingresar tipo, gr o ml', verbose_name='Tipo unidad ingrediente')
    imagen_ingre = models.CharField(max_length=300, default='Ingresar link imagen', verbose_name='Link imagen ingrediente')
    fecha_creacion_ingre = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion_ingre = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Ingrediente'
        verbose_name_plural='Ingredientes'
        ordering=['marca_ingre']

    def __str__(self):
        return f"{self.id_ingre} - {self.descripcion_ingre}"
    
class Ingredientes_preparacion(models.Model):
    id_prep = models.ForeignKey('Preparacion', on_delete=models.SET_DEFAULT, default='Blank', related_name='id_preparacion')
    id_ingre = models.ForeignKey('Ingrediente', on_delete=models.SET_DEFAULT, default='Blank', related_name='id_ingrediente')
    cantidad_necesaria = models.IntegerField(verbose_name='Cantidad necesaria', null=False, default=999)
    tipo_unidad = models.CharField(max_length=10,null=False, default='Ingresar tipo unidad', verbose_name='Tipo unidad')
    
    class Meta:
        verbose_name='Ingredientes_prep'
        verbose_name_plural='Ingredientes_prep'
        ordering=['id_prep']

    def __str__(self):
        return f"prep:{self.id_prep} - ingre:{self.id_ingre}"
    
class Preparacion(models.Model):
    id_prep = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID Preparacion')
    nombre_prep = models.CharField(max_length=32,null=False, blank=False, default='Ingresar nombre', verbose_name='Nombre preparacion')
    descripcion_prep = models.CharField(max_length=300,null=False, blank=False, default='Ingresar descripcion', verbose_name='Descripcion preparacion')
    imagen_prep = models.CharField(max_length=300, default='Ingresar link imagen', verbose_name='Link imagen preparacion')
    # stock_prep = models.IntegerField(null=False, default=0, verbose_name='Stock preparacion')
    id_cat_prep = models.ForeignKey('Categoria', on_delete=models.SET_DEFAULT, default='Blank', related_name='id_categoria')
    precio_prep = models.IntegerField(null=False, default=0, verbose_name='Precio preparacion')
    class Meta:
        verbose_name='Preparacion'
        verbose_name_plural='Preparacion'
        ordering=['nombre_prep']

    def __str__(self):
        return f"{self.id_prep} - {self.nombre_prep}"