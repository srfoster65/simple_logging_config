"""
Test Levels.

These test cases test the appropriate log level is set up for each handler
"""

import logging

import pytest

from simple_logging_config import configure_logging
from simple_logging_config import LoggingHandlerException


logger = logging.getLogger(__name__)


@pytest.fixture(scope="function", autouse=True)
def configure():
    """
    Ensure logging is reset after each test.
    """
    yield
    configure_logging().reset()


class TestLevels:
    """
    Class to test default config for simple_logging_config is correctly instantiated.
    """

    @pytest.mark.parametrize(
        "verbose, expected_level", [(0, 25), (1, 20), (2, 10), (3, 5)]
    )
    def test_verbose(self, verbose, expected_level):
        """
        Test verbosity param sets default handler level.
        """
        configure_logging(verbose=verbose)
        handler = logging.getLogger().handlers[0]
        assert handler.level == expected_level

    @pytest.mark.parametrize(
        "levels, expected_level", [(25, 25), (20, 20), (10, 10), (5, 5), ("20", 20)]
    )
    def test_set_integer_level(self, levels, expected_level):
        """
        Test setting default handler level as an integer.
        """
        configure_logging(levels=levels)
        handler = logging.getLogger().handlers[0]
        assert handler.level == expected_level

    @pytest.mark.parametrize(
        "levels, expected_level",
        [("TRACE", 5), ("DEBUG", 10), ("INFO", 20), ("PRINT", 25)],
    )
    def test_set_named_level(self, levels, expected_level):
        """
        Test setting default handler level as a string.
        """
        configure_logging(levels=levels)
        handler = logging.getLogger().handlers[0]
        assert handler.level == expected_level

    @pytest.mark.parametrize(
        "levels, expected_values",
        [
            ("{'console': 20}", {"console": 20}),
            ("{'console': '20'}", {"console": 20}),
            ("{'console': 'INFO'}", {"console": 20}),
            ("{'file': 5}", {"file": 5}),
            ("{'console': 20, 'file': 5}", {"console": 20, 'file': 5}),
            ("{'console': 20, 'file': 'TRACE'}", {"console": 20, 'file': 5}),
        ],
    )
    def test_set_dict_levels(self, levels, expected_values):
        """
        Test setting default handler level as a string.
        """
        configure_logging(levels=levels)
        handlers = logging.getLogger().handlers
        for handler_name, expected_level in expected_values.items():
            for handler in handlers:
                if handler.name == handler_name:
                    assert handler.level == expected_level

    @pytest.mark.parametrize(
        "levels, expected_values",
        [
            ("20", {"console": 20}),
            ("INFO", {"console": 20}),
            ("{'console': 20}", {"console": 20}),
            ("{'console': '20'}", {"console": 20}),
            ("{'console': 'INFO'}", {"console": 20}),
            ("{'file': 5}", {"file": 5}),
            ("{'console': 20, 'file': 5}", {"console": 20, 'file': 5}),
            ("{'console': 20, 'file': 'TRACE'}", {"console": 20, 'file': 5}),
        ],
    )
    def test_set_levels_by_env(self, levels, expected_values):
        """
        Test config can be selected via environment variable.
        """
        with pytest.MonkeyPatch.context() as mp:
            mp.setenv("SLC_LEVELS", levels)
            configure_logging()
            handlers = logging.getLogger().handlers
            for handler_name, expected_level in expected_values.items():
                print("handler_name=", handler_name)
                for handler in handlers:
                    if handler.name == handler_name:
                        assert handler.level == expected_level

    @pytest.mark.parametrize(
        "levels",
        [
            ("undefined_level"),
            ("['bad_type']"),
        ],
    )
    def test_bad_levels(self, levels):
        """
        Test verbosity param sets default handler level.
        """
        with pytest.raises(ValueError):
            configure_logging(levels=levels)


    @pytest.mark.parametrize(
        "levels",
        [
            ("{'undefined_handler': 10}"),
        ],
    )
    def test_bad_handler_in_level(self, levels):
        """
        Test a bad handler name raises exception
        """
        with pytest.raises(LoggingHandlerException):
            configure_logging(levels=levels)
