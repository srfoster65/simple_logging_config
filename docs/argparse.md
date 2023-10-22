# ArgParse Support

If you write CLI programs using ArgumentParser, support is included to simplify configuring logging in a standard fashion.


## add_logging_arguments(parser)

Calling add_logging_arguments(parser) with a parser object as a parameter will add the following paramters to your script.

- verbose
- slc-levels
- slc-modules
- slc-log-file-path
- slc-backup-count
- slc-config

Having called parser.parse_args(), the return value can be passed into the constructor of SimpleLoggingConfig as follows:

```python
SimpleLoggingConfig(**vars(args))
```

The following example shows how to add logging support to your CLI program.

```python
# test.py

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
usage: test.py [-h] [-v | --slc-levels [SLC_LEVELS ...]] [--slc-modules [SLC_MODULES ...]] [--slc-log-file-path SLC_LOG_FILE_PATH] [--slc-backup-count SLC_BACKUP_COUNT]
               [--slc-config {dual,dual_rotating,dual_detailed,console,file,rotating_file}]

Example Program

options:
  -h, --help            show this help message and exit
  -v, --verbose         The level of logging verbosity for the default handler. Use multiple times (up to -vvv) for increased      
                        verbosity.
  --slc-level LEVELS, --slc-levels LEVELS
                        The log level(s) to be applied to attached handlers. This value can be a single integer or a string        
                        representing a defined log level. Or it can be a string representing a dictionary where key/value pairs    
                        are handler names and the log level to be associated with that handler
  --slc-modules [MODULES ...]
                        The names of the modules to be logged. If omitted all modules are logged.
  --slc-log-file-path LOG_FILE_PATH
                        The path the log file will be saved to. If this is a folder, the log file will be saved to this folder     
                        with the file name derived from the name of the calling script. Otherwise, assume this is a full path to   
                        a named log file.
  --slc-backup-count BACKUP_COUNT
                        An integer specifying The number of backup log files to retain.
  --slc-config {dual,dual_rotating,dual_detailed,console,file,rotating_file}
                        The name of the logging config to be used.
```
