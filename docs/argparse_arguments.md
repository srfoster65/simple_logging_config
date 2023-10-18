# Add Logging Arguments to a Parser

If you write CLI programs using ArgumentParser, support is included to simplify configuring logging in a standard fashion.



## add_logging_arguments(parser)

Calling add_logging_arguments() with a parser object as a parameter will add the following paramters to your script.

- verbose
- slc_levels
- slc_modules
- slc_log_file_path
- slc_backup_count
- slc_config

Having called parser.parse_args(), the return value can be passed into the constructor of SimpleLoggingConfig as follows:

```python
SimpleLoggingConfig(**vars(args))
```

The following example shows how to add logging support to your CLI program.

```python
from argparse import ArgumentParser
from simple_logging_config import add_logging_arguments
from simple_logging_config import SimpleLoggingConfig

parser = ArgumentParser(description='Example Program')
add_logging_arguments(parser)

args = parser.parse_args()
SimpleLoggingConfig(**vars(args))

# Call your code here
```

Running the above program with the -h param will result in the following output

```text
usage: test.py [-h] [-v | --slc_levels [SLC_LEVELS ...]] [--slc_modules [SLC_MODULES ...]] [--slc_log_file_path SLC_LOG_FILE_PATH] [--slc_backup_count SLC_BACKUP_COUNT]
               [--slc_config {dual,dual_rotating,dual_detailed,console,file,rotating_file}]

Example Program

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
