#  pylint: disable=missing-module-docstring

import logging

from ._level import set_levels
from .simple_logging_config import SimpleLoggingConfig
from .add_logging_arguments import add_logging_arguments
from .add_logging_level import (
    add_logging_level,
    add_print_logging_level,
    add_trace_logging_level,
)

# Add a NullHander for the package
logging.getLogger(__name__).addHandler(logging.NullHandler())


# Define external API
__all__ = [
    "SimpleLoggingConfig",
    "set_levels",
    "add_logging_arguments",
    "add_logging_level",
    "add_print_logging_level",
    "add_trace_logging_level",
]
