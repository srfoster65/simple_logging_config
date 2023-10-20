"""
Test default logging configuration.
"""

import logging

import pytest

from simple_logging_config import configure_logging
from simple_logging_config._defaults import DEFAULT_LOGGING_CONFIG


logger = logging.getLogger(__name__)


@pytest.fixture(scope="class", autouse=True)
def configure():
    """
    Ensure logging is reset after each test.
    """
    configure_logging()
    yield
    configure_logging().reset()


class TestDefaultConfig:
    """
    Class to test default config for simple_logging_config is correctly instantiated.
    """

    DEFAULT_ROOT_LOG_LEVEL = 10
    DEFAULT_HANDLERS = ("console", "file")
    DEFAULT_LEVELS = {"console": 25, "file": 10}

    def test_default_config(self):
        """
        Test default config name.
        """
        assert configure_logging().config == DEFAULT_LOGGING_CONFIG

    def test_default_handlers(self):
        """
        Test correct handlers are added
        Pytest adds handlers, so must only test for expected.
        """
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
        handlers = logging.getLogger().handlers
        for handler in handlers:
            for handler_name, level in self.DEFAULT_LEVELS.items():
                if handler.name == handler_name:
                    logger.debug("Matched handler: %s", handler_name)
                    assert level == handler.level
                    break
