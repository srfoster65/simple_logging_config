# Usage

## Installation

With Pip:

```text
pip install simple_logging_config
```

## Recommended Usage

Logging should only be configured once for any script/program execution. With this in mind, SimpleLoggingConfig() is intended to be initialised when CLI scripts are executed. To facilitate this, helper methods are also included to configure ArgumentParser to provide a default set of ArgumentParser options to configure logging.

There are multiple ways to configure logging.

1. [Environment Variables](env_variables.md)
1. [ArgumentParser Options](argparse_arguments.md)
1. [Using the API](api.md)

See [Argparse Support](argparse_arguments.md) for details.
