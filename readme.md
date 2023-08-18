# SimpleLoggingConfig

## Overview

The SimpleLoggingConfig package provides simplified logging configuration.

To use with the default configuration, only 2 lines of code are required.

```python
from simple_logging_config import SimpleLoggingConfig

SimpleLoggingConfig()
```

This will enable **info** level logging to the console and **debug**  level logging to a file.

Information logged to the console is just the log message with no additional detail.
Information logged to file includes the timestamp, log_level, module and message

For a slightly more complex usecase, using a few additional lines of code, SimpleLoggingConfig is fully configurable using command line parameters.

```python
parser = ArgumentParser()
add_logging_arguments(parser)
args = parser.parse_args()

SimpleLoggingConfig(**vars(args))
```

## Detailed Usage

SimpleLoggingConfig() takes 6 optional parameters

+ verbose: Similar to slc_levels. An integter representing the verbosity level. 0: Default, 1: Info, 2: Debug, 3: Trace
+ slc_levels: The log level to use for the primary (first defined) handler.
+ slc_modules: A list of modules that logging should be enabled for
+ slc_log_file_path: The location where a log file should be created (if applicable).
+ slc_backup_count: The number of backup log files to keep (if applicable).
+ slc_config: The name of the logging configuration to use.

Additionally, behaviour can also be modified by the of environemnt variables. Some behaviours can ONLY be updated by the use of environemnt variables.

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

4 configurations are provided

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
It is not possible to change the formatter associated with the handler.

### Formatters

There are 2 formatters defined for the various configs.

+ brief: Logs only the message.
+ verbose: Logs timestamp, log_level, module and the message.

Formatters can be modified by the use of environment variables.

Create an environment variable with the name: SLC_[HANDLER_NAME]_FORMAT, where HANDLER_NAME is the name of a defined handler, in uppercase. e.g. CONSOLE, FILE or ROTATING_FILE

e.g. To display the log level along with the message for the console logging handler.

```text
set SLC_CONSOLE_FORMAT=%(levelname)s %(message)s
```

Note: Setting this value incorrectly may cause logging to raise an exception.

## Additional Features

### Set Logging Level

To modify the logging level after SimpleLoggingConfig has been configured use set_level().
This call takes a list of values, where the 1st value is applied to the first handler, etc.
A value of None or "-" will leave the level unchanged for that handler.
If less values are supplied than handlers, then only the handlers for which a level is provided will be updated.

The following call will set the output of the first handler to DEBUG and the output of the second handler to TRACE level.

```python
SimpleLoggingConfig.set_level(["DEBUG", "TRACE"])
```

## Adding Custom Logging Levels

Several helper functions are provided to support adding additional custom log levels.

+ Only CLI programs should configure the logger.
+ No library can assume additional loggers have been defined

With this in mind, any library module that wishes to use an additional logging level should register the additional level itself. It should not assume that logging has been configured as it may have been called by directly by a script that has not used SimpleLoggingConfig.

### Add Print Logging Level

The PRINT log level sits between "INFO" and "WARNING" and is defined as level 25. It is intended for information that should be output always, but is not at the WARNING severity.

Add the following to any module that requires access to the "PRINT" logging level

```python
from simple_logging_config import add_print_logging_level

add_print_logging_level()

logging.getLogger(__name__).print('Hello World')
```

Note: The calling script would need to set the logging level of the appropriate handler to ensure the print messages are recorded, although this would not normally be required for this level of logging.

### Add Trace Logging Level

The TRACE log level sits between "DEBUG" and "NOTSET" and is defined as level 5. It is intended for very detailed information that would make DEBUG logging too verbose. It would almost always never be set unless debugging a specific problem.

Add the following to any module that requires access to the "TRACE" logging level

```python
from simple_logging_config import add_trace_logging_level

add_trace_logging_level()

logging.getLogger(__name__).trace('Trace Message')
```

Note: The calling script would need to set the logging level of the appropriate handler to ensure the trace messages are recorded.

### Add a Custom Logging Level

This allows adding a custom logging level to any module.

```python
from simple_logging_config import add_logging_level

add_logging_level('custom', 2)

logging.getLogger(__name__).custom('Custom Message')
```

## Add Logging Arguments to a Parser

If you write CLI programs using ArgumentParser, support is included to simplify configuring logging in a standard fashion.

The following example shows how to add logging support to your CLI program.

```python
from argparse import ArgumentParser
from simple_logging_config import add_logging_arguments
from simple_logging_config import SimpleLoggingConfig

parser = ArgumentParser(description='Example Program')
args = parser.parse_args()

SimpleLoggingConfig(**vars(args))

# Call your code here
```

Running the above program with the -h param will result in the following output

```text
usage: test.py [-h] [-v | --slc_levels [SLC_LEVELS ...]] [--slc_modules [SLC_MODULES ...]] [--slc_log_file_path SLC_LOG_FILE_PATH] [--slc_backup_count SLC_BACKUP_COUNT]
               [--slc_config {dual,dual_rotating,dual_detailed,console,file,rotating_file}]

Test Program

options:
  -h, --help            show this help message and exit
  -v, --verbose         The level of logging verbosity for the default handler. Use multiple times (up to -vvv) for increased verbosity.
  --slc_levels [SLC_LEVELS ...]
                        The log levels to be applied to attached handlers. The levels are applied to the handlers in the order the handlers are registered. To skip a handler, use 'None'
                        or '-'.
  --slc_modules [SLC_MODULES ...]
                        The names of the modules to be logged.
  --slc_log_file_path SLC_LOG_FILE_PATH
                        The path the log file will be saved to. If this is a path, the log file will be saved to this path with the file name derived from the name of the calling script.
                        Otherwise, assume this a path to a named log file.
  --slc_backup_count SLC_BACKUP_COUNT
                        An integer specifying The number of backup log files to retain.
  --slc_config {default,detailed,console,file}
                        The name of the logging config to be used.
```

## Example Usage

### Log debug messages to the console

```python
SimpleLoggingConfig('debug')
```

or

```python
SimpleLoggingConfig(10)
```

### Log debug messages to the console and trace messages to file

```python
SimpleLoggingConfig(['debug', 'trace'])
```

### Leave console log level unchanged and Log trace messages to file

```python
SimpleLoggingConfig(['None', 'trace'])
```

or

```python
SimpleLoggingConfig(['-', 'trace'])
```

### Only Log messages for the package 'MyPackage'

```python
SimpleLoggingConfig(slc_modules=['MyPackage'])
```

### Log debug messages to the console only for the package 'MyPackage'

```python
SimpleLoggingConfig('debug', slc_modules=['MyPackage'])
```

### Save the log to a file named my_log.log in the current working directory

```python
SimpleLoggingConfig(slc_path='my_log')
```

### Keep multiple backup copies of the log file

```python
SimpleLoggingConfig(slc_backup_count=5)
```

### Log messages only to file

```python
SimpleLoggingConfig(slc_config='file')
```

### A more complex use case

Any combination of parameters can be combined to achieve the desired logging configuration.

+ Log debug messages to the console.
+ Only Log messages for the package 'MyPackage'.
+ Keep multiple backup copies of the log file.
+ Save the log to a file named my_log.log in the current working directory.
+ Use the config 'detailed'

```python
SimpleLoggingConfig('debug', slc_modules=['MyPackage'], slc_backup_count=5, slc_path='my_log', slc_config='detailed)
```
