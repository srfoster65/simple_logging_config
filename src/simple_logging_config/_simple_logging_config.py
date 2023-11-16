"""
Class that configures logging to provide support for a selection of console
and file logging handlers.

Config:
The "dual" config is used if not specified. The config can be adusted by
parameters or the  environment variable defined by: SLC_DEFAULT_CONFIG

Level
Where a config logs to multiple handlers, the level of each handler can be
adjusted by supplying level as a list of values.

Modules
Logging can be restricted to specific modules by providing a list of module
names.
"""
#  pylint: disable=no-member

import logging
import logging.config
from typing import Any

from arg_init import ClassArgInit, ArgDefaults

from ._add_logging_level import add_print_logging_level, add_trace_logging_level
from ._defaults import (
    DEFAULT_LOG_FILE_PATH,
    DEFAULT_LOG_FILE_BACKUP_COUNT,
    DEFAULT_LOGGING_CONFIG,
    ENV_PREFIX,
    VERBOSE_MAPPING,
)
from ._file import rotate_log, modify_log_file_attributes
from ._filters import filter_module_logging
from ._formatters import modify_formatters
from ._logging_config import get_logging_config
from ._level import set_log_levels
from ._singleton import Singleton

from pathlib import Path


logger = logging.getLogger(__name__)


class SimpleLoggingConfig(metaclass=Singleton):
    """
    Class to simplify logging configuration
    """

    # pylint:  disable=unused-argument
    def __init__(
        self,
        config: str | None = None,
        verbose: bool | None = None,
        levels: int | str | None = None,
        modules: list[str] | None = None,
        log_file_path: Path | None = None,
        backup_count: int | None = None,
        **kwargs: Any,
    ) -> None:
        """
        Configure logging to provide default logging facilities.
        """
        defaults = [
            ArgDefaults("config", default_value=DEFAULT_LOGGING_CONFIG),
            ArgDefaults("log_file_path", default_value=DEFAULT_LOG_FILE_PATH),
            ArgDefaults("backup_count", default_value=DEFAULT_LOG_FILE_BACKUP_COUNT),
        ]
        ClassArgInit(env_prefix=ENV_PREFIX, defaults=defaults)
        config_data = get_logging_config(self.config)
        modify_formatters(config_data)
        modify_log_file_attributes(config_data, self._log_file_path, self._backup_count)  # type: ignore[attr-defined]
        logging.config.dictConfig(config_data)
        # Take a copy of current handlers in case other modules add more later.
        # i.e. pytest. This is to allow the tearing down (reset) of SLC.
        self._handlers = logging.getLogger().handlers.copy()
        self.rotate()
        filter_module_logging(self._modules)  # type: ignore[attr-defined]
        add_print_logging_level()
        add_trace_logging_level()
        self.set_levels(self._levels if self._levels else VERBOSE_MAPPING.get(self._verbose))  # type: ignore[attr-defined]
        self._report_logging_config()

    def set_levels(self, levels: int | str | None) -> None:
        """
        Set Logging levels
        log levels can be adjusted after initialisation.
        """
        set_log_levels(levels)

    def rotate(self) -> None:
        """
        rotate log files.
        """
        rotate_log(self._handlers)

    @property
    def config(self) -> str:
        """Return the currently configure logging config."""
        return self._config  # type: ignore[attr-defined]

    def reset(self) -> None:
        """
        This API is provided primarily for unit testing. It is not intended for general use
        """
        logger.debug("Reset simple_logging_config")
        for handler in self._handlers:
            logger.debug("removing handler: %s", handler.name)
            handler.close()
            logging.root.removeHandler(handler)
        SimpleLoggingConfig.clear()

    def __str__(self) -> str:
        return "\n".join(self._info())

    def __repr__(self) -> str:
        return f"<SimpleLoggingConfig(config={self.config})>"

    def _info(self) -> list[str]:
        info = [f"Logging config: {self.config}"]
        for handler in self._handlers:
            info.append(f"  {handler}")
        return info

    def _report_logging_config(self) -> None:
        for item in self._info():
            logger.debug(item)
