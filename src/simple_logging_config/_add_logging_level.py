"""
Add custom log levels to the logging class.
"""

import logging

from ._defaults import (
    PRINT_LOGGING_LEVEL,
    PRINT_LOGGING_NAME,
    TRACE_LOGGING_LEVEL,
    TRACE_LOGGING_NAME,
)


def add_logging_level(level_name: str, level: int) -> None:
    """Add support for a new logging level."""

    def log_for_level(self, message, *args, **kwargs):  # pragma: no cover
        if self.isEnabledFor(level):
            # Note: self._log takes *args parameter as args
            self._log(  # pylint: disable=protected-access
                level, message, args, **kwargs
            )

    def log_to_root(message, *args, **kwargs):  # pragma: no cover
        logging.log(level, message, args, **kwargs)

    level_function = level_name.lower()
    logging.addLevelName(level, level_name)
    setattr(logging, level_name, level)
    setattr(logging.getLoggerClass(), level_function, log_for_level)
    setattr(logging, level_function, log_to_root)


def add_print_logging_level() -> None:
    """Add support for a PRINT logging level."""
    add_logging_level(PRINT_LOGGING_NAME, PRINT_LOGGING_LEVEL)


def add_trace_logging_level() -> None:
    """Add support for a TRACE logging level."""
    add_logging_level(TRACE_LOGGING_NAME, TRACE_LOGGING_LEVEL)
