"""
Logging filters
"""

import logging


logger = logging.getLogger(__name__)


class Whitelist(logging.Filter):
    """
    Logging filter to only log messages from named modules
    """
    def __init__(self, modules):
        super().__init__()
        self.whitelist = [logging.Filter(module) for module in modules]

    def filter(self, record):
        return any(f.filter(record) for f in self.whitelist)


def filter_module_logging(modules) -> None:
    """
    Add specified modules to the filter whitelist
    """
    if modules:
        logger.debug('Adding modules to filter whitelist: %s', modules)
        for handler in logging.root.handlers:
            handler.addFilter(Whitelist(modules))
