"""
Test default logging configuration.
"""

import logging

import pytest

from simple_logging_config import configure_logging


logger = logging.getLogger(__name__)


@pytest.fixture(scope="class", autouse=True)
def configure():
    """
    Ensure logging is reset after each test.
    """
    # configure_logging()
    yield
    configure_logging().reset()


class TestDefaultConfig:
    """
    Class to test default config for simple_logging_config is correctly instantiated.
    """
    DEFAULT_ROOT_LOG_LEVEL = 10
    DEFAULT_HANDLERS = ("console", "file")
    DEFAULT_LEVELS = {"console": 25, "file": 10}

    def test_str(self):
        """
        Test first line of str() returns correct string
        """
        slc = configure_logging()
        out = str(slc)
        assert ("Logging config: dual" in out)

    def test_repr(self):
        """
        Test repr() returns correct string
        """
        slc = configure_logging()
        out = repr(slc)
        assert "<SimpleLoggingConfig(config=dual)>" == out
