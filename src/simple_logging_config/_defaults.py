"""
Constants used by SimpleLoggingConfig
"""

import logging

ENV_PREFIX = "SLC"

# Environment variable names
# All environment variable names start with the prefix as defined by ENV_PRFIX
DEFAULT_VERBOSITY_ENV = "_".join([ENV_PREFIX, "VERBOSITY"])
DEFAULT_LOG_LEVELS_ENV =  "_".join([ENV_PREFIX, "LOG_LEVELS"])
DEFAULT_LOGGING_MODULES_ENV =  "_".join([ENV_PREFIX, "MODULES"])
DEFAULT_LOG_FILE_PATH_ENV =  "_".join([ENV_PREFIX, "LOG_FILE_PATH"])
DEFAULT_LOG_FILE_BACKUP_COUNT_ENV =  "_".join([ENV_PREFIX, "LOG_FILE_BACKUP_COUNT"])
DEFAULT_LOGGING_CONFIG_ENV =  "_".join([ENV_PREFIX, "CONFIG"])
CUSTOM_FORMAT_TEMPLATE_ENV =  "_".join([ENV_PREFIX, "{handler_name}", "FORMAT"])

# Default values
DEFAULT_LOG_FILE_PATH = "."
DEFAULT_LOG_FILE_BACKUP_COUNT = 5
DEFAULT_LOGGING_CONFIG = "dual"

# Additional pre-defined logging levels
PRINT_LOGGING_LEVEL = logging.INFO + 5
PRINT_LOGGING_NAME = "PRINT"
TRACE_LOGGING_LEVEL = logging.DEBUG - 5
TRACE_LOGGING_NAME = "TRACE"


# Map the verbosity level to a logging level
VERBOSE_MAPPING = {0: None, 1: 20, 2: 10, 3: 5}  # Not set, Info, Debug, Trace
