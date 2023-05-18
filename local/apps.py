from django.apps import AppConfig


class LocalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'local'

    # def ready(self):
    #     import local.signals