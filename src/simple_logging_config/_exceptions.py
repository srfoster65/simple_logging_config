"""
Exceptions raised by SimpleLoggingConfig
"""


class InvalidLoggingConfigException(Exception):
    """Exception raised for an invalid config resource name"""
    def __init__(self, config_name):
        super().__init__(f"Invalid Logging Config: {config_name}")


class InvalidResourceException(Exception):
    """Exception raised for an invalid config resource name"""
    def __init__(self, resource_name):
        super().__init__(f"Invalid Resource Name: {resource_name}")


class InvalidHandlerException(Exception):
    """Exception raised for an invalid config resource name"""
    def __init__(self, handler_name):
        super().__init__(f"Invalid Handler: {handler_name}")
