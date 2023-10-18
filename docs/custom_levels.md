# Custom Logging Levels

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
