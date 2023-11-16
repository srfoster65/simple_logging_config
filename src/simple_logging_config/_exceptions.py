"""Exceptions raised by simple_logging_config."""


class SLCError(Exception):
    """Base class for all simple_logging_config exceptions."""


class LoggingConfigError(SLCError):
    """Exception raised for an invalid config resource name."""

    def __init__(self, config_name: str) -> None:
        super().__init__(f"Invalid Logging Config: {config_name}")


class LoggingHandlerError(SLCError):
    """Exception raised for an invalid handler name."""

    def __init__(self, handler_name: str) -> None:
        super().__init__(f"Invalid Handler: {handler_name}")
