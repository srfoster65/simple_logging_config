# Overview

[![tests][tests_badge]][tests_url]
[![codecov][codecov_badge]][codecov_url]
[![Docs][docs_badge]][docs_url]
[![PyPI][pypi_badge]][pypi_url]
[![PyPI - License][license_badge]][license_url]

## Installation

With Pip:

```text
pip install simple_logging_config
```

## Usage

The simple_logging_config package provides a simplified logging configuration.

To use with the default configuration, only 2 lines of code are required.

```python
from simple_logging_config import configure_logging

configure_logging()
```

Or

```python
from simple_logging_config import SimpleLoggingConfig

SimpleLoggingConfig()
```

This will enable **info** level logging to the console and **debug** level logging to a file.

Information logged to the console is just the log message with no additional detail.  
Information logged to file includes the timestamp, log_level, module and message

For a slightly more complex usecase, using a few additional lines of code, configure_logging is configurable using command line parameters.

```python
# myscript.py

from argparse import ArgumentParser
from simple_logging_config import configure_logging, add_logging_arguments

parser = ArgumentParser(description="Test Program")
add_logging_arguments(parser)
args = parser.parse_args()

configure_logging(**vars(args))
```

Your script will now accept additional CLI paramaters to configure logging at runtime as shown below.

```python
usage: myscript.py [-h] [-v | --slc-level LEVELS] [--slc-modules [MODULES ...]] [--slc-log-file-path LOG_FILE_PATH]
               [--slc-backup-count BACKUP_COUNT] [--slc-config {dual,dual_rotating,dual_detailed,console,file,rotating_file}]      

Test Program

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

[tests_badge]: https://github.com/srfoster65/simple_logging_config/actions/workflows/build.yml/badge.svg
[tests_url]: https://github.com/srfoster65/simple_logging_config/actions/workflows/build.yml
[codecov_badge]: https://codecov.io/gh/srfoster65/simple_logging_config/graph/badge.svg?token=FFNWSCS4BB
[codecov_url]: https://codecov.io/gh/srfoster65/simple_logging_config
[docs_badge]: https://github.com/srfoster65/simple_logging_config/actions/workflows/docs.yml/badge.svg
[docs_url]: https://srfoster65.github.io/simple_logging_config/
[pypi_badge]: https://img.shields.io/pypi/v/simple-logging-config?logo=python&logoColor=%23cccccc
[pypi_url]: https://pypi.org/project/simple-logging-config
[license_badge]: https://img.shields.io/pypi/l/simple-logging-config
[license_url]: https://srfoster65.github.io/simple_logging_config/license/
