"""
Test printing functions
"""

import logging

from simple_logging_config import configure_logging


logger = logging.getLogger(__name__)


class TestPrintFunctions:
    """
    Class to test default config .
    """

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
