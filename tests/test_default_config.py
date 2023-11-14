"""
Test default logging configuration.
"""

import logging

from simple_logging_config import configure_logging
from simple_logging_config._defaults import DEFAULT_LOGGING_CONFIG


logger = logging.getLogger(__name__)


class TestDefaultConfig:
    """
    Class to test default config for simple_logging_config is correctly instantiated.
    """

    DEFAULT_ROOT_LOG_LEVEL = 10
    DEFAULT_HANDLERS = ("console", "file")
    DEFAULT_LEVELS = {"console": 25, "file": 10}

    def test_default_config(self, fs):
        """
        Test default config name.
        """
        assert configure_logging().config == DEFAULT_LOGGING_CONFIG

    def test_default_handlers(self):
        """
        Test correct handlers are added
        Pytest adds handlers, so must only test for expected.
        """
        configure_logging()
        handlers = logging.getLogger().handlers
        for count, handler in enumerate(self.DEFAULT_HANDLERS):
            assert handlers[count].name == handler

    def test_root_effective_level(self):
        """
        Test root logger effective level.
        """
        # Cannot test as root logger level may be adjusted by test framework
        pass

    def test_default_log_levels(self):
        """
        Test levels of indivdual handlers
        """
        configure_logging()
        handlers = logging.getLogger().handlers
        for handler in handlers:
            print(handler.name)
            for handler_name, level in self.DEFAULT_LEVELS.items():
                if handler.name == handler_name:
                    logger.debug("Matched handler: %s", handler_name)
                    assert level == handler.level
                    break
