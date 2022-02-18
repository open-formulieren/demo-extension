from django.db import models
from django.utils.translation import gettext_lazy as _

from solo.models import SingletonModel


class DemoExtensionConfig(SingletonModel):
    """
    global configuration and defaults
    """

    demo_field = models.CharField(_("demo field"), max_length=250)
