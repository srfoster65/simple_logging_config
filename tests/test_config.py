"""
Test configuration methods
"""

import pytest

from simple_logging_config import configure_logging


class TestConfiguration:
    """
    Class to test log to file functions
    """

    def test_config_by_arg(self):
        """
        Test config can be initialised by arg "config"
        """
        config = "console"
        slc = configure_logging(config=config)
        assert slc.config == config

    def test_config_by_env(self):
        """
        Test config can be initialised by env SLC_CONFIG
        """
        config = "console"
        with pytest.MonkeyPatch.context() as mp:
            mp.setenv("SLC_CONFIG", config)
            slc = configure_logging()
            assert slc.config == config

    def test_config_by_toml_config_file(self, fs):
        """
        Test config can be initialised by file "config.toml"
        """
        config = "console"
        toml_config = f"[SimpleLoggingConfig]\nconfig='{config}'"
        fs.create_file("config.toml", contents=toml_config)
        slc = configure_logging()
        assert slc.config == config
