"""
Test filtering of log messages for a specific module.

These test cases check that logging is correctly configured, not that the messages are
correctly filtered.
"""

import logging

from simple_logging_config import configure_logging


logger = logging.getLogger(__name__)


class TestFilters:
    """
    Class to test default config for simple_logging_config is correctly instantiated.
    """

    def test_filter(self):
        """
        Test config can be selected via environment variable.
        """
        expected = ["test2", "test1"]
        slc = configure_logging(modules=["test2", "test1"])
        handlers = logging.getLogger().handlers
        for handler in handlers:
            print(handler.name)
            for filter in handler.filters:
                for count2, module in enumerate(filter.whitelist):
                    print(count2, expected[count2])
                    assert module.name == expected[count2]
        slc.reset()
