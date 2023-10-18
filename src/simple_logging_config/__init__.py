#  pylint: disable=missing-module-docstring

import logging


from ._add_logging_arguments import add_logging_arguments
from ._add_logging_level import (
    add_logging_level,
    add_print_logging_level,
    add_trace_logging_level,
)
from ._configure import configure_logging
from ._configure import reset_logging
from ._configure import print_logging_config
from ._exceptions import InvalidLoggingConfigException, InvalidResourceException
from ._level import set_levels
from ._simple_logging_config import SimpleLoggingConfig

# Add a NullHander for the package
logging.getLogger(__name__).addHandler(logging.NullHandler())


# Define Public API
__all__ = [
    "SimpleLoggingConfig",
    "configure_logging",
    "reset_logging",
    "print_logging_config",
    "set_levels",
    "add_logging_arguments",
    "add_logging_level",
    "add_print_logging_level",
    "add_trace_logging_level",
    "InvalidLoggingConfigException",
    "InvalidResourceException",
]
