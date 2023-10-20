"""
Test support for modifying default formatters.

Warning:
This relies on accessing a private method of logging so may break in a future release
"""

import logging

import pytest

from simple_logging_config import configure_logging


logger = logging.getLogger(__name__)


class TestFormatters:
    """
    Class to formatters can be set via envs .
    """

    def test_formatter(self, caplog):
        """
        Test a formatter can be set from an environment variable
        """
        env = "SLC_CONSOLE_FORMAT"
        env_value = "Test format %(message)s"
        with pytest.MonkeyPatch.context() as mp:
            mp.setenv(env, env_value)
            configure_logging()
            assert "Test format" in caplog.text
