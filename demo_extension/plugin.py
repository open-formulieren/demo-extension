from typing import TYPE_CHECKING

from django.utils.translation import ugettext_lazy as _

from openforms.conf.utils import config
from openforms.registrations.base import BasePlugin
from openforms.registrations.exceptions import NoSubmissionReference
from openforms.registrations.registry import register

from .config import DemoExtensionOptionsSerializer
from .models import DemoExtensionConfig

if TYPE_CHECKING:
    from openforms.submissions.models import Submission


@register("demo_extension")
class DemoRegistration(BasePlugin):
    verbose_name = _("Demo Extension - print to console")
    configuration_options = DemoExtensionOptionsSerializer
    is_demo_plugin = True

    def register_submission(self, submission: "Submission", options: dict) -> None:
        print(submission)

        # Demo usage of dynamics configuration
        demo_config = DemoExtensionConfig.get_solo()
        print(f"Demo dynamic config value: {demo_config.demo_field}")

        # Demo usage of options
        if options.get("demo_option"):
            print(f"Demo option value: {options['demo_option']}")

        # Demo usage of environment variables
        demo_env_var = config("DEMO_ENV_VAR", "")
        if demo_env_var:
            print(f"Demo environment variable: {demo_env_var}")

    def get_reference_from_result(self, result: None) -> None:
        raise NoSubmissionReference("Demo plugin does not emit a reference")

    def update_payment_status(self, submission: "Submission", options: dict):
        print(submission)

    def check_config(self):
        """
        Demo config is always valid.
        """
        pass
