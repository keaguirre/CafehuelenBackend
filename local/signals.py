from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Local, Totem, Superv_local

# @receiver(pre_save, sender=Totem)
# def asignar_numero_totem(sender, instance, **kwargs):
#     if instance.num_totem == 0:
#         # Obtiene el último número de totem utilizado
#         ultimo_totem = Totem.objects.order_by('-num_totem').first()
#         if ultimo_totem:
#             nuevo_numero_totem = ultimo_totem.num_totem + 1
#         else:
#             nuevo_numero_totem = 1

#         # Asigna el nuevo número de totem
#         instance.num_totem = nuevo_numero_totem
