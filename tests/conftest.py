"""
Common fixtures used for all test cases
"""
from pathlib import Path

import pytest

from simple_logging_config import configure_logging

# package root is used to allow mapping of package resources into fake fs
package_root = Path(__file__).parent.parent.resolve()


@pytest.fixture(scope="function", autouse=True)
def reset():
    """
    Ensure logging is reset at the end of all tests. This will be executed even if there
    are errors in individual tests and ensures subsequent test classes are not effected
    """
    yield
    slc = configure_logging()
    slc.reset()


@pytest.fixture(scope="function", autouse=True)
def configure_fs(fs):
    """
    Use a fake fs and map in required resources.
    """
    fs.add_real_directory(Path(package_root, "src/simple_logging_config/resources"))
    yield fs
