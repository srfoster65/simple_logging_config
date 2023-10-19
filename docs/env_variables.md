# General Information

All environment variables have the prefix **SLC_** to minimise the risk of a namespace clash.

Environment variables must be set before logging is initialised.

## Priority

When logging is initialised, the following precedence applies:

1. Environment Variable
1. Argument value
1. Implementation default

## Supported Environment Variables

### SLC_DEFAULT_CONFIG

Define the default configuration to be used when initialising logging.

The value should be a string that represents a valid logging configuration.

### SLC_DEFAULT_LOG_LEVELS

Define the default logging levels to be used for each handler.

The value should be a string, or list of strings, with a value for each handler. Values are applied to handlers in order. Once the list of values is used up, remaining handlers keep their originally configured log level.

### SLC_DEFAULT_MODULES

Define the python modules that logging should be enabled for. Only defined modules will emit logging messages. Log levels still apply to the associated handlers.

The value should be a string, or list of strings.

### SLC_DEFAULT_LOG_FILE_PATH

Define the folder or path and file name that log files should be written to.

The value should be string.

Note: This has no effect if no file handlers are defined.

### SLC_DEFAULT_LOG_FILE_BACKUP_COUNT

Define the number of backup files to maintain if using a rotating file handler.

Note: This has no effect if no rotating file handlers are defined.

### SLC_{handler_name}_FORMAT

Define a custom logging message format for a specific handler.

The value should be a string that python logging can interpret.

Note: Use with caution: This string is not validated. If defined incorrectly, this could cause logging to raise an exception.
