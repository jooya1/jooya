from django.apps import AppConfig


class ThingsConfig(AppConfig):
    name = 'things'

    def ready(self):
        import things.signals
