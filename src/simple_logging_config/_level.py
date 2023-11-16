"""Functions related setting the logging level."""

import logging
from ast import literal_eval

from ._exceptions import LoggingHandlerError

logger = logging.getLogger(__name__)


def _handler_lvl(level: int) -> dict[str, int]:
    """Return a key value pair of the the name of the first log handler and the value parameter."""
    handlers = logging.getLogger().handlers
    if len(handlers) > 0:
        handler = logging.getLogger().handlers[0]
        if handler.name:  # Satisfy mypy
            return {handler.name: level}
    return {}


def _eval(levels: int | str) -> dict[str, int | str]:
        if isinstance(levels, str):  # to satisfy mypy
            levels_dict = literal_eval(levels)
            if isinstance(levels_dict, dict):
                return levels_dict
        raise ValueError


def _get_handler_levels(levels: int | str | None) -> dict[str, int]:
    """
    Return a dict mapping handler names to logging levels.

    levels can be a single int/string representing a log level
    or a string representation of a dictionary of handler names to level mappings.
    e.g. The following are all valid
      levels = 5
      levels = "DEBUG"
      levels = "{'console': 20, 'file': 'TRACE'}"
    """
    if levels:
        # if isinstance(levels, int):
        try:
            # test if levels is a simple log level name represenation
            level = _log_level_to_int(levels)
            return _handler_lvl(level)
        except AttributeError:
            # test if levels can be parsed as a dictionary
            levels_dict = _eval(levels)
            return {handler_name: _log_level_to_int(level) for handler_name, level in levels_dict.items()}
    return {}


def _log_level_to_int(level: int | str) -> int:
    """Return a named log level as an integer."""
    try:
        return int(level)
    except ValueError:
        return getattr(logging, level.upper())  # type: ignore[union-attr]


def _display_level(level: int) -> str:
    """Return a string representing the level name and the integer value of the level."""
    level_str = logging.getLevelName(level)
    return f"{level_str} ({level})"


def _set_root_log_level(levels: dict[str, int]) -> None:
    """Update the root log level with lowest log level."""
    if levels:
        level = min([_log_level_to_int(level) for level in levels.values()])
        root_logger = logging.getLogger()
        if level < root_logger.getEffectiveLevel():
            logger.debug("Setting root logging level to %s", _display_level(level))
            root_logger.setLevel(level)


def _set_handler_log_levels(levels: dict[str, int]) -> None:
    """Update logging handler levels."""
    handlers = logging.getLogger().handlers
    for handler_name, level in levels.items():
        for handler in handlers:
            if handler.name == handler_name:
                int_lvl = _log_level_to_int(level)
                logger.debug(
                    "Setting handler level: %s = %s",
                    handler.name,
                    _display_level(int_lvl),
                )
                handler.setLevel(level)
                break
        else:
            raise LoggingHandlerError(handler_name)


def set_log_levels(levels: int | str | None) -> None:
    """Adjust logging levels for root logger and attached handlers."""
    handler_lvls = _get_handler_levels(levels)
    _set_root_log_level(handler_lvls)
    _set_handler_log_levels(handler_lvls)
