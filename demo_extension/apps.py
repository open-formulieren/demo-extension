from django.apps import AppConfig


class DemoExtensionConfig(AppConfig):
    name = "demo_extension"

    def ready(self):
        from . import plugin # noqa
