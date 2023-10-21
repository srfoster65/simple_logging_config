# Usage

## Installation

With Pip:

```text
pip install simple_logging_config
```

## Recommended Usage

Logging should only be configured once for any script/program execution. With this in mind, simple_logging_config is intended to be initialised when CLI scripts are executed. To facilitate this, helper methods are also included to configure ArgumentParser to provide a default set of ArgumentParser options to configure logging.

There are multiple ways to configure logging.

1. [Environment Variables](env_variables.md)
1. [ArgumentParser Options](argparse.md)
1. [Using the API](api/reference.md)

## CLI Usage

The following example shows how to add support to a CLI script. This enables logging in the script, along with the ability to adjust logging behaviour via command line parameters.

```python

from argparse import ArgumentParser
from simple_logging_config import configure_logging, add_logging_arguments

parser = ArgumentParser()
add_logging_arguments(parser)
args = parser.parse_args()

configure_logging(**vars(args))

# your code here
```

See [Argparse Support](argparse.md) for details of the parameters available.
