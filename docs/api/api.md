# Using the API

## configure_logging

This is the primary API used to configure logging for a script/program.

configure_logging() takes 6 optional parameters

+ verbose: Similar to slc_levels. An integter representing the verbosity level. 0: Default, 1: Info, 2: Debug, 3: Trace
+ slc_levels: The log level(s) to use.
+ slc_modules: A list of modules that logging should be enabled for
+ slc_log_file_path: The location where a log file should be created (if applicable).
+ slc_backup_count: The number of backup log files to keep (if applicable).
+ slc_config: The name of the logging configuration to use.

Additionally, behaviour can also be modified by the use of environemnt variables.
Note: Some behaviours can ONLY be updated by the use of environemnt variables.

```python
from simple_logging_config import configure_logging

configure_logging()
```

See [API Examples](api_examples.md) for more detialed use cases.

### Handler Logging Levels

slc_levels sets the log level for each handler defined in the selected config. The first value is applied to the first handler, etc. If less values are supplied than attahced handlers then the remaining handlers log level is unchanged.
Each level can be an integer or string defining a configured level. If a value of None (or '-') is specified then the level is unchanged.

#### Handler Logging Level Defaults

If no parameter is provided then the environment variable "SLC_DEFAULT_LOG_LEVEL" will be used.
If no environment variable is defined then the logging levels are unchanged.

### Modules

slc_modules is a list of modules names that logging should be enabled for. No other modules will emit any log messages.
Default behaviour is to enable logging for all modules.

#### Module Defaults

If no parameter is provided then the environment variable "SLC_DEFAULT_MODULES" will be used.
If no environemnt variable is provided, logging shall be enabled for all modules

### Path

The path (or filename) to use when logging to file (if applicable). If file logging is not supported by the selected config this parameter is ignored.
If path is a folder, the the log is saved to this folder, using the name of the calling script, with a ".log" suffix.
Else it is assumed that path specifies a filename that should be used to save the log to.

#### Path Defaults

If no paramter is provided then the environment variable "LOGGING_DEFAULT_LOG_FILE_PATH" will be used.
If no environment variable is defined then the log file will be saved to the current working directory with the name of the calling script and a .log file extension.

The path can be selected when initialising SimpleLoggingConfig for the first time. Once set it cannot be changed.
This parameter has no effect if used with a config that does not support logging to file.

### Backup Count

The number of backup copies of the log file to retain.
This defaults to 0. i.e. No backups are retained.

#### Backupcount Defaults

If no paramter is provided then the environment variable "LOGGING_DEFAULT_LOG_FILE_BACKUP_COUNT" will be used.
If no environment variable is defined then no backups will be retained

The backup count can be set when initialising SimpleLoggingConfig for the first time. Once set it cannot be changed.
This parameter has no effect if used with a config that does not support logging to file.

### Config

The name of the config to use for logging.

Several configurations are provided:

+ dual:
  + console handler - brief : INFO
  + file handler - detailed : DEBUG
+ dual_detailed:
  + console handler - detailed : INFO
  + file handler - detailed : DEBUG
+ dual_rotating:
  + console handler - brief : INFO
  + rotating file handler - detailed : DEBUG
+ console:
  + console handler - detailed : DEBUG
+ file:
  + file handler - detailed : DEBUG
+ rotating_file:
  + rotating file handler - detailed : DEBUG

#### Config Defaults

If no paramter is provided then the environment variable "LOGGING_DEFAULT_CONFIG" will be used.
If no environment variable is defined then the config named "dual" will be used.

The config can be selected when initialising SimpleLoggingConfig for the first time. Once selected it cannot be changed.


### Formatters

There are 2 formatters defined for the various configs.

+ brief: Logs only the message.
+ verbose: Logs timestamp, log_level, module and the message.

Formatters can be modified by the use of environment variables. If a custom formatter is required, the environemnt variable must be set before logging is initialised.

Create an environment variable with the name: SLC_[HANDLER_NAME]_FORMAT, where HANDLER_NAME is the name of a defined handler, in uppercase. e.g. CONSOLE, FILE or ROTATING_FILE

e.g. To display the log level along with the message for the console logging handler.

```text
set SLC_CONSOLE_FORMAT=%(levelname)s %(message)s
```

Note: Setting this value incorrectly may cause logging to raise an exception.

## print_logging_config

Display information relating to the current logging configuration.

```python
from simple_logging_config import print_logging_config

print_logging_config()
```

## Set Logging Level

To modify the logging level after SimpleLoggingConfig has been configured use set_level().
This call takes a list of values, where the 1st value is applied to the first handler, etc.
A value of None or "-" will leave the level unchanged for that handler.
If less values are supplied than handlers, then only the handlers for which a level is provided will be updated.

The following call will set the output of the first handler to DEBUG and the output of the second handler to TRACE level.

```python
from simple_logging_config import configure_logging
from simple_logging_config import set_level

configure_logging()
set_level(["DEBUG", "TRACE"])
```
