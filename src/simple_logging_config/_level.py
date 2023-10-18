"""
Functions related setting the logging level.
"""

from os import getenv
from ast import literal_eval
import logging


logger = logging.getLogger(__name__)


def _get_log_levels(levels: int | str | None) -> dict:
    """
    Return a dict mapping handler names to logging levels

    levels can be a single int/string representing a log level
    or a string representation of a dictionary of handler names to level mappings.
    e.g. The following are all valid
      levels = 5
      levels = "DEBUG"
      levels = "{'console': 20, 'file': 'TRACE'}"
    """
    if levels:
        try:
            # test if levels is a simple log level (int or string represenation)
            level = _log_level_to_int(levels)
            handler = logging.getLogger().handlers[0]
            return {handler.name: level}
        except (ValueError, AttributeError):
            try:
                # test if levels can be parsed as a dictionary
                levels_dict = literal_eval(levels)
                if isinstance(levels_dict, dict):
                    return {
                        handler_name: _log_level_to_int(level)
                        for handler_name, level in levels_dict.items()
                    }
                raise ValueError(f"Invalid value for log level: {levels}") from None
            except Exception:
                raise ValueError(f"Invalid value for log level: {levels}") from None
    return {}


def _log_level_to_int(level: int | str) -> int:
    """
    Return a named log level as an integer.
    """
    try:
        return int(level)
    except ValueError:
        int_level = getattr(logging, level)
        if isinstance(int_level, int):
            return int_level
    raise ValueError(f"Invalid log level: {level}")


def _display_level(level: int | str) -> str:
    """
    Return a string representing the level name and the integer value of the level.
    """
    if isinstance(level, int):
        level_str = logging.getLevelName(level)
    else:
        level_str = level
        level = logging.getLevelName(level_str)
    return f"{level_str} ({level})"


def _set_root_log_level(levels: dict) -> None:
    """
    Update the root log level with lowest log level.
    """
    if levels:
        level = min([_log_level_to_int(level) for level in levels.values()])
        root_logger = logging.getLogger()
        if level < root_logger.getEffectiveLevel():
            logger.debug("Setting root logging level to %s", _display_level(level))
            root_logger.setLevel(level)


def _set_handler_log_levels(levels: dict) -> None:
    """
    Update logging handler levels
    """
    handlers = logging.getLogger().handlers
    for handler_name, level in levels.items():
        for handler in handlers:
            if handler.name == handler_name:
                level = _log_level_to_int(level)
                logger.debug(
                    "Setting handler level: %s = %s",
                    handler.name,
                    _display_level(level),
                )
                handler.setLevel(level)
                break
        else:
            logger.warning("No handler for: %s", handler_name)


def set_levels(levels: int | str | None) -> None:
    """
    Adjust logging levels for root logger and attached handlers.
    """
    levels = _get_log_levels(levels)
    _set_root_log_level(levels)
    _set_handler_log_levels(levels)
