from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Categoria, Preparacion, Detalle_preparacion

@receiver(pre_save, sender=Categoria)
def update_preparaciones_on_categoria_state_change(sender, instance, **kwargs):
    if instance.pk:
        # Obtener el estado anterior de la categoría
        old_categoria = Categoria.objects.get(pk=instance.pk)
        old_estado = old_categoria.estado

        if old_estado and not instance.estado:
            # La categoría pasó de estado True a False
            # Desactivar todas las preparaciones asociadas a esta categoría
            Preparacion.objects.filter(id_cat_prep=instance.id_cat).update(estado=False)

@receiver(post_save, sender=Preparacion)
def update_detalles_on_preparacion_state_change(sender, instance, **kwargs):
    if instance.pk:
        old_preparacion = Preparacion.objects.get(pk=instance.pk)
        old_estado = old_preparacion.estado

        if old_estado and not instance.estado:
            # La preparación pasó de estado True a False
            # Desactivar todos los detalles de preparación asociados a esta preparación
            Detalle_preparacion.objects.filter(id_prep=instance.id_prep).update(estado=False)
