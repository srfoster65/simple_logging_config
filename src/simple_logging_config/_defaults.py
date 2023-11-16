"""Constants used by SimpleLoggingConfig."""

import logging

ENV_PREFIX = "SLC"

# Environment variable names
CUSTOM_FORMAT_TEMPLATE_ENV = f"{ENV_PREFIX}_{{handler_name}}_FORMAT"

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
