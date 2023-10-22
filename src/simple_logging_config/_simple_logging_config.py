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

from arg_init import ArgInit, Arg

from ._add_logging_level import add_print_logging_level, add_trace_logging_level
from ._defaults import (
    DEFAULT_LOG_FILE_PATH,
    DEFAULT_LOG_FILE_BACKUP_COUNT,
    DEFAULT_LOGGING_CONFIG,
    ENV_PREFIX,
    VERBOSE_MAPPING,
)
from ._exceptions import LoggingHandlerException
from ._file import rotate_log, modify_log_file_attributes
from ._filters import filter_module_logging
from ._formatters import modify_formatters
from ._logging_config import get_logging_config
from ._level import set_levels
from ._singleton import Singleton


logger = logging.getLogger(__name__)


class SimpleLoggingConfig(metaclass=Singleton):
    """
    Class to simplify logging configuration
    """

    # pylint:  disable=unused-argument
    def __init__(
        self,
        config=None,
        verbose=None,
        levels=None,
        modules=None,
        log_file_path=None,
        backup_count=None,
        **kwargs
    ) -> None:
        """
        Configure logging to provide default logging facilities.
        """
        args = (
            Arg("config", default=DEFAULT_LOGGING_CONFIG),
            Arg("log_file_path", default=DEFAULT_LOG_FILE_PATH),
            Arg("backup_count", default=DEFAULT_LOG_FILE_BACKUP_COUNT),
        )
        ArgInit(env_prefix=ENV_PREFIX, func_is_bound=True, args=args)
        config_data = get_logging_config(self.config)
        modify_formatters(config_data)
        modify_log_file_attributes(config_data, self._log_file_path, self._backup_count)
        logging.config.dictConfig(config_data)
        # Take a copy of current handler names in case other modules add more
        # later i.e. pytest. This is to allow the tearing down (reset) of SLC.
        self._handlers = [handler.name for handler in logging.getLogger().handlers]
        rotate_log()
        filter_module_logging(self._modules)
        add_print_logging_level()
        add_trace_logging_level()
        set_levels(self._levels if self._levels else VERBOSE_MAPPING.get(self._verbose))
        self._report_logging_config()

    @property
    def config(self):
        return self._config

    def reset(self) -> None:
        """
        This API is provided primarily for unit testing. It is not intended for general use
        """
        logger.debug("Reset simple_logging_config")
        logger.debug("Removing handlers: %s", self._handlers)
        for handler_name in self._handlers:
            handler = self._get_handler(handler_name)
            handler.close()
            logging.root.removeHandler(handler)
        SimpleLoggingConfig.clear()

    def __str__(self):
        return "\n".join(self._info())

    def __repr__(self):
        return f"<SimpleLoggingConfig(config={self.config})>"

    def _info(self) -> list:
        info = [f"Logging config: {self.config}"]
        for handler_name in self._handlers:
            info.append(f"  {str(self._get_handler(handler_name))}")
        return info

    def _report_logging_config(self) -> None:
        for item in self._info():
            logger.debug(item)

    def _get_handler(self, handler_name: str | None):
        for handler in logging.getLogger().handlers:
            if handler.name == handler_name:
                return handler
        raise LoggingHandlerException(handler_name)
