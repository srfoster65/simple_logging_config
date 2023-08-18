"""
Constants used by SimpleLoggingConfig
"""

import logging


# Environment variable names
# All environment variable names start with the prefix SLC_
DEFAULT_LOG_LEVELS_ENV = "SLC_DEFAULT_LOG_LEVELS"
DEFAULT_LOGGING_MODULES = "SLC_DEFAULT_MODULES"
DEFAULT_LOG_FILE_PATH_ENV = "SLC_DEFAULT_LOG_FILE_PATH"
DEFAULT_LOG_FILE_BACKUP_COUNT_ENV = "SLC_DEFAULT_LOG_FILE_BACKUP_COUNT"
DEFAULT_LOGGING_CONFIG_ENV = "SLC_DEFAULT_CONFIG"
CUSTOM_FORMAT_TEMPLATE_ENV = "SLC_{handler_name}_FORMAT"

# Additional pre-defined logging levels
PRINT_LOGGING_LEVEL = logging.INFO + 5
PRINT_LOGGING_NAME = "PRINT"
TRACE_LOGGING_LEVEL = logging.DEBUG - 5
TRACE_LOGGING_NAME = "TRACE"

DEFAULT_LOGGING_CONFIG = "dual"
DEFAULT_LOG_FILE_PATH = "."

# Map the verbosity level to a logging level
VERBOSE_MAPPING = {
    0: None,  # Not set
    1: 20,    # Info
    2: 10,    # Debug
    3:  5     # Trace
}
