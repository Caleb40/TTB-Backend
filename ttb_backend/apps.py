from django.apps import AppConfig


class TtbBackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ttb_backend'

    def ready(self):
        import ttb_backend.signals
