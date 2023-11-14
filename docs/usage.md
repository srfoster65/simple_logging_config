# Usage

## Installation

With Pip:

```text
pip install simple_logging_config
```

## Recommended Usage

Logging should only be configured once for any script/program execution. With this in mind, simple_logging_config is intended to be initialised when CLI scripts are executed. To facilitate this, helper methods are also included to configure ArgumentParser to provide a default set of ArgumentParser options to configure logging.

There are two ways to configure logging.

1. [ArgumentParser Options - CLI](argparse.md)
2. [Direct - API](api/reference.md)

Any [environment variables](/env_variables/) that are set will take precedence over arguments provided via the CLI or API.

## CLI Usage

The following example shows how to add support to a CLI script. This enables logging in the script, along with the ability to adjust logging behaviour via command line parameters. Additaionally, any SLC_* environment variables that are defined will be used when logging is initialised. See [here](/env_variables/) for more information.

```python
# myscript.py

from argparse import ArgumentParser
from simple_logging_config import configure_logging, add_logging_arguments

parser = ArgumentParser()
add_logging_arguments(parser)
args = parser.parse_args()

configure_logging(**vars(args))

# your code here
```

e.g.

Running **myscript.py** with the following options will enable debug logging to console.

```text
python myscript.py -vv
```

See [Argparse Support](argparse.md) for details of the parameters available.

Note: Any script specific arguments can be safely passed to configure_logging, and these will simply be ignored. The only requirement being they do not clash with any simple_logging_config argument names.

## API Usage

The following example shows how to configure logging via the API to use the dual_rotating configuration.
Additaionally, any SLC_* environment variables that are defined will be used when logging is initialised. See [here](/env_variables/) for more information.

```python
from simple_logging_config import configure_logging

configure_logging(config="dual_rotating")

# your code here
```
