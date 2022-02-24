from unittest.mock import patch

from django.test import TestCase

from openforms.forms.tests.factories import FormFactory
from openforms.submissions.tests.factories import SubmissionFactory

from ..models import DemoExtensionConfig
from ..plugin import DemoRegistration


class DemoExtensionTests(TestCase):
    @patch("demo_extension.plugin.config")
    @patch("demo_extension.plugin.test_function")
    @patch("demo_extension.plugin.DemoExtensionConfig.get_solo")
    def test_options_in_demo_extension(self, m_solo, m_test_function, m_config):
        m_solo.return_value = DemoExtensionConfig(demo_field="Solo config value")
        m_config.return_value = "Env variable value"
        form_options = {"demo_option": "Form specific option"}

        form = FormFactory.create(
            generate_minimal_setup=True,
            registration_backend="demo_extension",
        )
        submission = SubmissionFactory.create(form=form)

        demo_submission = DemoRegistration("demo_extension")
        demo_submission.register_submission(submission, form_options)

        m_test_function.assert_called_with(
            "Solo config value", "Form specific option", "Env variable value"
        )
