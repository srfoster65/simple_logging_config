# SimpleLoggingConfig

## Installation

With Pip:

```text
pip install simple_logging_config
```

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
from argparse import ArgumentParser
from simple_logging_config import SimpleLoggingConfig, add_logging_arguments

parser = ArgumentParser()
add_logging_arguments(parser)
args = parser.parse_args()

SimpleLoggingConfig(**vars(args))
```
