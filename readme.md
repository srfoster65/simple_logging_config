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

For a slightly more complex usecase, using a few additional lines of code, SimpleLoggingConfig is configurable using command line parameters.

```python
from argparse import ArgumentParser
from simple_logging_config import SimpleLoggingConfig, add_logging_arguments

parser = ArgumentParser()
add_logging_arguments(parser)
args = parser.parse_args()

SimpleLoggingConfig(**vars(args))
```

Your script will now accept additional CLI paramaters to configure logging at runtime.

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
