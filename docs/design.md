# Design

## Implementation

simple_logging_config creates logging handlers at the root level. This means that these handlers will be available to all modules unless specifically overridden.

### Handlers

3 types of handlers are defined

- Console
- File
- Rotating File

### Formatters

2 message output formats are defined

- Brief
- Detailed

Note: It is possiible to customise the output format for a specific handler using environment variables.

### Pre-defined Configs

Combinations of these options are made available via pre-defined configurations

1. dual
    - console: brief
    - file: detailed
2. dual_detailed
    - console: detailed
    - file: detailed
3. dual_rotating
    - console: brief
    - rotating_file: detailed
4. console
    - console: detailed
5. file
    - file: detailed
6. rotating_file
    - rotating_file: detailed
