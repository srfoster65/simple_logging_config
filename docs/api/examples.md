
# API Example Usage

## Log debug messages to the console

Using the verbose option

```python
configure_logging(verbose=2)
```

Or using a named log level

```python
configure_logging(levels='debug')
```

or using a numeric value

```python
configure_logging(levels=10)
```

## Log debug messages to the console and trace messages to file

```python
configure_logging(levels ={"console": 'debug', "file": 'trace'})
```

## Leave console log level unchanged and log trace messages to file

```python
configure_logging({"file": 'trace'})
```

## Only Log messages for the package 'MyPackage'

```python
configure_logging(modules=['MyPackage'])
```

## Log debug messages to the console only for the package 'MyPackage'

```python
configure_logging(levels='debug', modules=['MyPackage'])
```

## Save the log to a file named my_log.log in the current working directory

```python
configure_logging(log_file_path='my_log')
```

## Keep 3 backup copies of the log file

```python
configure_logging(config="dual_rotating", backup_count=3)
```

## Log messages only to file

```python
configure_logging(config='file')
```

## A more complex use case

Any combination of parameters can be combined to achieve the desired logging configuration.

+ Log debug messages to the console.
+ Only Log messages for the package 'MyPackage'.
+ Save all logs in a folder named logs (folder must already exist)
+ Keep 10 backup copies of the log file.
+ Use the config 'dual_rotating'

```python
configure_logging(levels='debug', modules=['MyPackage'], log_file_path='logs', backup_count=10, config='dual_rotating)
```
