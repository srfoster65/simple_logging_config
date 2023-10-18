"""
Functions related to modifying logging formatters

Overide default formatters for specific handlers with new format read from environment variables.
"""

from os import environ

from ._defaults import CUSTOM_FORMAT_TEMPLATE_ENV


def modify_formatters(config_data: dict) -> None:
    """
    Overide default formatters for specific handlers with new format read from environment variables.
    """
    for handler_name in config_data["handlers"]:
        format_str = environ.get(
            CUSTOM_FORMAT_TEMPLATE_ENV.format(handler_name=handler_name)
        )
        if format_str is not None:
            formatter_name = "custom_" + handler_name
            # Add a custom formatter
            config_data["formatters"][formatter_name] = {}
            config_data["formatters"][formatter_name]["format"] = format_str
            # Use the custom formatter in the named handler
            config_data["handlers"][handler_name]["formatter"] = formatter_name
