"""
Exceptions raised by SimpleLoggingConfig
"""

class SLCException(Exception):
    pass


class LoggingConfigException(SLCException):
    """Exception raised for an invalid config resource name"""
    def __init__(self, config_name):
        super().__init__(f"Invalid Logging Config: {config_name}")


class LoggingResourceException(SLCException):
    """Exception raised for an invalid config resource name"""
    def __init__(self, resource_name):
        super().__init__(f"Invalid Resource Name: {resource_name}")


class LoggingHandlerException(SLCException):
    """Exception raised for an invalid config resource name"""
    def __init__(self, handler_name):
        super().__init__(f"Invalid Handler: {handler_name}")
