"""
Construct the logging config dictionary.
"""

from importlib.resources import files
from pathlib import Path

from jinja2 import Environment, PackageLoader
import yaml

from ._exceptions import LoggingConfigException

LOGGING_CONFIG = "src/simple_logging_config/resources/default.yaml.jinja"
RESOURCE_PATH = str(Path("resources", "{resource_name}"))


def _resource_path(resource_name: str) -> str:
    return RESOURCE_PATH.format(resource_name=resource_name)


def _read_resource(resource_name: str):
    my_resources = files(__package__)
    resource_path = _resource_path(resource_name)
    return (my_resources / resource_path).read_bytes()


def _read_yaml_resource(resource_name):
    return yaml.safe_load(_read_resource(resource_name))


def _read_definitions() -> dict:
    return {
        "handlers": _read_yaml_resource("handlers.yaml"),
        "formatters": _read_yaml_resource("formatters.yaml"),
    }


def read_configs() -> dict:
    """
    Read configs.yaml resource
    """
    return _read_yaml_resource("configs.yaml")


def get_logging_config(config_name) -> dict:
    """
    Return a logging dictionary config as specified by config_name
    """
    try:
        config_data = read_configs()[config_name]
    except KeyError:
        raise LoggingConfigException(config_name) from None
    data = {
        "definitions": _read_definitions(),
        "config": config_data,
    }
    env = Environment(
        loader=PackageLoader("simple_logging_config", "resources"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("default.yaml.jinja")
    logging_config = template.render(data)
    return yaml.safe_load(logging_config)
