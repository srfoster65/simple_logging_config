"""
Helper functions
"""

from ._simple_logging_config import SimpleLoggingConfig


def configure_logging(**kwargs) -> SimpleLoggingConfig:
    """External API to initialise logging."""
    return SimpleLoggingConfig(**kwargs)
