"""Helper functions."""

from typing import Any

from ._simple_logging_config import SimpleLoggingConfig


def configure_logging(**kwargs: Any) -> SimpleLoggingConfig:  # noqa: ANN401
    """External API to initialise logging."""
    return SimpleLoggingConfig(**kwargs)
