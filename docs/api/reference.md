# Reference

## configure_logging

```python
configure_logging(config=None, verbose=None, levels=None, modules=None, log_file_path=None, backup_count=None, **kwargs) -> SimpleLoggingConfig
```

This is the primary API used to configure logging for a script/program.
Returns a SimpleLoggingConfig object

configure_logging() takes 6 optional parameters

+ verbose: An integter representing the verbosity level.
+ levels: The log level(s) to use.
+ modules: A list of modules that logging should be enabled for.
+ log_file_path: The location where a log file should be created (if applicable).
+ backup_count: The number of backup log files to keep (if applicable).
+ config: The name of the logging configuration to use.

Additionally, behaviour can also be modified by the use of environment variables.

Note: Names use "_" separator in the function signature as opposed to "-" in command line parameters.  
Note: Some behaviours can **only** be updated by the use of environemnt variables.

See [API Examples](examples.md) for example use cases.

### Handler Logging Levels

The options **verbose** and **levels** are mutually exclusive. Both can be used to adjust the logging levels. If levels is defined then this will be used in preference to verbose.

#### verbose

Verbose is an integer used to change the logging level of the default handler:

+ 0: unchanged
+ 1: info
+ 2: debug
+ 3: trace

#### Verbose Defaults

If no parameter is provided then the environment variable "SLC_VERBOSE" will be used.
If no environment variable is defined then the logging levels are unchanged.

#### levels

levels sets the log level for specific handlers.  
This can either a single value or a dictionary where the key is the name of the handler and the value the level to apply to that handler. If a single value is provided, this is applied to the default handler. The level value can be an integer or string representing a named level.

e.g.

+ levels=20
+ levels="info"
+ levels={"console": "debug", "file": "debug"}

#### Handler Logging Level Defaults

If no parameter is provided then the environment variable "SLC_LEVELS" will be used.
If no environment variable is defined then the logging levels are unchanged.

### Modules

modules is a list of modules names that logging should be enabled for. No other modules will emit any log messages. If this value is unset then logging will be enabled for all modules.
Default behaviour is to enable logging for all modules.

#### Module Defaults

If no parameter is provided then the environment variable "SLC_MODULES" will be used.
If no environemnt variable is provided, logging shall be enabled for all modules

### Log File Path

log_file_path is used to set the path (or filename) to use when logging to file. If file logging is not supported by the selected config this parameter is ignored.
If log_file_path is an existing folder, the log is saved to this folder, using the name of the calling script, with a ".log" suffix. Else it is assumed that log_file_path specifies a filename that should be used to save the log to in the current working directory.

#### Log File Path Defaults

If no paramter is provided then the environment variable "SLC_LOG_FILE_PATH" will be used.  
If no environment variable is defined then the log file will be saved to the current working directory with the name of the calling script and a .log file extension.

The path can be selected when initialising SimpleLoggingConfig for the first time. Once set it cannot be changed.

This parameter has no effect if used with a config that does not support logging to file.

### Backup Count

backup_count is the number of backup copies of log files to retain.

#### Backup Count Defaults

If no paramter is provided then the environment variable "SLC_BACKUP_COUNT" will be used.  
If no environment variable is defined this default to 5.

This parameter has no effect if used with a config that does not support rotating file handlers.

### Config

The name of the config to use for logging.

The following are supported configs and their associated handlers and formats used for each handler:

+ **dual:**
    + console handler - brief : INFO
    + file handler - detailed : DEBUG
+ **dual_detailed:**
    + console handler - detailed : INFO
    + file handler - detailed : DEBUG
+ **dual_rotating:**
    + console handler - brief : INFO
    + rotating file handler - detailed : DEBUG
+ **console:**
    + console handler - detailed : DEBUG
+ **file:**
    + file handler - detailed : DEBUG
+ **rotating_file:**
    + rotating file handler - detailed : DEBUG

#### Config Defaults

If no paramter is provided then the environment variable "SLC_CONFIG" will be used.
If no environment variable is defined then the config named "dual" will be used.

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

## SimpleLoggingConfig

### Initialisation

```python
SimpleLoggingConfig(config=None, verbose=None, levels=None, modules=None, log_file_path=None, backup_count=None, **kwargs)
```

The class used to implement logging configuration

An instance of SimpleLoggingConfig is returned by configure_logging(), or it can be initialised directly.

### Methods

#### Set Levels

Used to adjust logging levels post initialisation.

```python
set_levels(levels)
```

Where level is a single value or a dictionary. If a single value is provided, this is applied to the default handler. If a dictionary is provided, the key represents the name of the handler and the value the log level to apply to that handler. The level value can be an integer or string representing a named level.

#### Rotate

Call doRollover on any handlers that support log rotation

```python
rotate()
```

#### Reset

Tear down SimpleLoggingConfig. Used for testing only

```python
reset()
```
