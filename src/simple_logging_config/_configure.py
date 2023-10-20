"""
Helper functions
"""

from ._simple_logging_config import SimpleLoggingConfig


def configure_logging(**kwargs) -> SimpleLoggingConfig:
    """External API to initialise logging."""
    return SimpleLoggingConfig(**kwargs)


def reset_logging(slc: SimpleLoggingConfig | None = None):  # pragma: no cover
    """Reset simple logging configuartion."""
    slc = slc or SimpleLoggingConfig()
    slc.reset()
