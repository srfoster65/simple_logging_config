"""
Test named configurations.

These test cases test the named configs setup the specified handlers at the correct logging levels.
"""

import logging

import pytest

from simple_logging_config import configure_logging
from simple_logging_config import LoggingConfigError

logger = logging.getLogger(__name__)


class TestNamedConfigs:
    """
    Class to test default config for simple_logging_config is correctly instantiated.
    """

    def test_named_config(self):
        """
        Test config can be selected via environment variable.
        """
        config = "console"
        slc = configure_logging(config=config)
        assert slc.config == config

    def test_set_config_by_env(self):
        """
        Test config can be selected via environment variable.
        """
        config = "console"
        with pytest.MonkeyPatch.context() as mp:
            mp.setenv("SLC_CONFIG", config)
            slc = configure_logging()
            assert slc.config == config

    def test_env_overrides_param(self):
        """
        Test config can be selected via environment variable.
        """
        arg_config = "file"
        env_config = "console"
        with pytest.MonkeyPatch.context() as mp:
            mp.setenv("SLC_CONFIG", env_config)
            slc = configure_logging(config=arg_config)
            assert slc.config == env_config

    @pytest.mark.parametrize(
        "config, expected",
        [
            ("dual", {"console": 25, "file": 10}),
            ("dual_detailed", {"console": 25, "file": 10}),
            ("dual_rotating", {"console": 25, "rotating_file": 10}),
            ("console", {"console": 25}),
            ("file", {"file": 10}),
            ("rotating_file", {"rotating_file": 10}),
        ],
    )
    def test_named_configs_detail(self, config, expected):
        """
        Test named configs initialise handlers and levels correctly.
        """
        slc = configure_logging(config=config)
        assert slc.config == config
        handlers = logging.getLogger().handlers
        for handler_name, level in expected.items():
            for handler in handlers:
                if handler.name == handler_name:
                    assert handler.level == level

    def test_bad_named_config(self):
        """
        Test exception raised if invalid config requested.
        """
        with pytest.raises(LoggingConfigError):
            configure_logging(config="bad_config_name")
