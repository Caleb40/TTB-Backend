from django.apps import AppConfig


class CoreAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_auth'

    def ready(self):
        import core_auth.signals
