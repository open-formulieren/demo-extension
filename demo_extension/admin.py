from django.contrib import admin

from solo.admin import SingletonModelAdmin

from .models import DemoExtensionConfig


@admin.register(DemoExtensionConfig)
class DemoExtensionConfigAdmin(SingletonModelAdmin):
    pass
