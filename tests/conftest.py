"""
Common fixtures used for all test cases
"""

import pytest

from simple_logging_config import configure_logging


@pytest.fixture(scope="class", autouse=True)
def configure():
    """
    Ensure logging at the end of all tests. This will be executed even if there
    are errors in individual tests and ensures subsequent test classes are not effected
    """
    yield
    slc = configure_logging()
    slc.reset()
