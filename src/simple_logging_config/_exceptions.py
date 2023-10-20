"""
Exceptions raised by SimpleLoggingConfig
"""


class SLCException(Exception):
    """Base class for all simple_logging_config exceptions"""


class LoggingConfigException(SLCException):
    """Exception raised for an invalid config resource name"""

    def __init__(self, config_name):
        super().__init__(f"Invalid Logging Config: {config_name}")


class LoggingHandlerException(SLCException):
    """Exception raised for an invalid handler name"""

    def __init__(self, handler_name):
        super().__init__(f"Invalid Handler: {handler_name}")
