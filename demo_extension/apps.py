from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DemoExtensionConfig(AppConfig):
    name = "demo_extension"
    label = "demo_extension"
    verbose_name = _("Demo extension registrations plugin")

    def ready(self):
        from . import plugin  # noqa
