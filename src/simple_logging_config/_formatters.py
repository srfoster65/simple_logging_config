"""
Functions related to modifying logging formatters

Overide default formatters for specific handlers with new format read from environment variables.
"""
import logging
from os import environ

from ._defaults import CUSTOM_FORMAT_TEMPLATE_ENV


logger = logging.getLogger(__name__)


def modify_formatters(config_data: dict) -> None:
    """
    Overide default formatters for specific handlers with new format read from environment variables.
    """
    for handler_name in config_data["handlers"]:
        logger.debug(CUSTOM_FORMAT_TEMPLATE_ENV)
        env_name =  CUSTOM_FORMAT_TEMPLATE_ENV.format(handler_name=handler_name).upper()
        logger.debug("Checking formatter: %s = %s", handler_name, env_name)
        format_str = environ.get(env_name)
        if format_str is not None:
            logger.debug("Updating formatter: %s = %s", handler_name, format_str)
            formatter_name = "custom_" + handler_name
            # Add a custom formatter
            config_data["formatters"][formatter_name] = {}
            config_data["formatters"][formatter_name]["format"] = format_str
            # Use the custom formatter in the named handler
            config_data["handlers"][handler_name]["formatter"] = formatter_name
