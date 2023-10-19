
# API Example Usage

## Log debug messages to the console

```python
configure_logging('debug')
```

or

```python
configure_logging(10)
```

## Log debug messages to the console and trace messages to file

```python
configure_logging(['debug', 'trace'])
```

## Leave console log level unchanged and Log trace messages to file

```python
configure_logging(['None', 'trace'])
```

or

```python
configure_logging(['-', 'trace'])
```

## Only Log messages for the package 'MyPackage'

```python
configure_logging(slc_modules=['MyPackage'])
```

## Log debug messages to the console only for the package 'MyPackage'

```python
configure_logging('debug', slc_modules=['MyPackage'])
```

## Save the log to a file named my_log.log in the current working directory

```python
configure_logging(slc_path='my_log')
```

## Keep multiple backup copies of the log file

```python
configure_logging(config="dual_rotating", slc_backup_count=5)
```

## Log messages only to file

```python
configure_logging(slc_config='file')
```

## A more complex use case

Any combination of parameters can be combined to achieve the desired logging configuration.

+ Log debug messages to the console.
+ Only Log messages for the package 'MyPackage'.
+ Keep multiple backup copies of the log file.
+ Save the log to a file named my_log.log in the current working directory.
+ Use the config 'dual_rotating'

```python
configure_logging('debug', slc_modules=['MyPackage'], slc_backup_count=5, slc_path='my_log', slc_config='dual_rotating)
```
