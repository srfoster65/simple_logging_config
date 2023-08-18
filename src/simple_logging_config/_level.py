"""
Functions related setting the logging level.
"""

from os import getenv
import logging

from .defaults import DEFAULT_LOG_LEVELS_ENV


logger = logging.getLogger(__name__)
SEPARATORS = ",;"
IGNORE_STRINGS = ("None", "-")


def _get_env(env_name) -> list:
    """
    Read the environment variable, remove any punctuation and split on space characters
    """
    env = getenv(env_name, "")
    stripped = env.translate(str.maketrans(SEPARATORS, " " * len(SEPARATORS)))
    return stripped.split()


def _get_log_levels(levels: int | str | list | None) -> dict:
    """
    Return a dict mapping handlers to logging levels
    """
    if levels is None:
        levels = _get_env(DEFAULT_LOG_LEVELS_ENV)
    if isinstance(levels, (int, str)):
        levels = [levels]
    handlers = logging.getLogger().handlers
    if len(levels) > len(handlers):
        raise ValueError("Too many level values supplied")
    return {
        handlers[count]: _log_level_to_int(level)
        for count, level in enumerate(levels)
        if level not in IGNORE_STRINGS
    }


def _log_level_to_int(level: int | str) -> int:
    """
    Transform level to an integer
    """
    try:
        return int(level)
    except ValueError:
        int_level = getattr(logging, level.upper(), 0)
        if int_level:
            return int_level
    raise ValueError(f"Invalid log level: {level}")


def _display_level(level):
    """
    Return a string representing the level name and the integer value of the level.
    """
    return f"{logging.getLevelName(level)} ({level})"


def _set_root_log_level(levels: list) -> None:
    """
    Update the level for the root logger
    """
    if levels:
        level = min(levels.values())
        root_logger = logging.getLogger()
        if level < root_logger.getEffectiveLevel():
            logger.debug("Setting root logging level to %s", _display_level(level))
            root_logger.setLevel(level)


def _set_handler_log_levels(levels: dict) -> None:
    """
    Update logging handler levels
    """
    for handler, level in levels.items():
        logger.debug(
            "Setting handler level: %s = %s", handler.name, _display_level(level)
        )
        handler.setLevel(level)


def set_levels(levels: int | str | list | None) -> None:
    """
    Adjust logging levels for root logger and attached handlers.
    """
    level_map = _get_log_levels(levels)
    _set_root_log_level(level_map)
    _set_handler_log_levels(level_map)
