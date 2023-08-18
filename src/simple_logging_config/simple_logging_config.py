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

from os import getenv
import logging
import logging.config

from .add_logging_level import add_print_logging_level, add_trace_logging_level
from .defaults import (
    DEFAULT_LOGGING_CONFIG_ENV,
    DEFAULT_LOGGING_CONFIG,
    VERBOSE_MAPPING,
)
from ._file import rotate_log, modify_log_file_attributes
from ._filters import filter_module_logging
from ._formatters import modify_formatters
from ._logging_config import get_logging_config
from ._level import set_levels
from ._singleton import Singleton


class SimpleLoggingConfig(metaclass=Singleton):
    """
    Class to immplement Simple Logging Config
    Do not instantiate this class directly. Instead, simply call the public
    function - configure()
    """

    def __init__(
        self,
        verbose: int = 0,
        *,
        slc_levels: int | str | list | None = None,
        slc_modules: str | list = None,
        slc_log_file_path: str | None = None,
        slc_backup_count: int | None = 0,
        slc_config: str | None = None,
        **kwargs,  # pylint: disable=unused-argument
    ) -> None:
        """
        Configure logging to provide default logging facilities.
        """
        self._config_name = slc_config or getenv(
            DEFAULT_LOGGING_CONFIG_ENV, DEFAULT_LOGGING_CONFIG
        )
        slc_levels = slc_levels if slc_levels else VERBOSE_MAPPING.get(verbose)
        config_data = get_logging_config(self._config_name)
        modify_formatters(config_data)
        modify_log_file_attributes(config_data, slc_log_file_path, slc_backup_count)
        logging.config.dictConfig(config_data)
        rotate_log()
        filter_module_logging(slc_modules)
        add_print_logging_level()
        add_trace_logging_level()
        set_levels(slc_levels)
        self._report_logging_config()

    def __str__(self):
        return '\n'.join(self._info())

    def __repr__(self):
        return f"<SimpleLoggingConfig(slc_config={self._config_name})>"

    def _info(self) -> list:
        info = [f"Logging config: {self._config_name}"]
        for handler in logging.getLogger().handlers:
            info.append(f"  {str(handler)}")
        return info

    def _report_logging_config(self) -> None:
        logger = logging.getLogger(__name__)
        for item in self._info():
            logger.debug(item)
