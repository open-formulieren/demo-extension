from django.utils.translation import ugettext_lazy as _

from openforms.utils.mixins import JsonSchemaSerializerMixin
from rest_framework import serializers


class DemoExtensionOptionsSerializer(JsonSchemaSerializerMixin, serializers.Serializer):
    demo_option = serializers.CharField(
        label=_("Demo extension option"),
        required=False,
    )
