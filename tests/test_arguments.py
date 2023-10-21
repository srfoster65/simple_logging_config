"""
Test ArgumentParser logging arguments
"""

from argparse import ArgumentParser
import logging

from simple_logging_config import add_logging_arguments


logger = logging.getLogger(__name__)


class TestPrintFunctions:
    """
    Class to test default config .
    """

    def test_arguments(self):
        """
        Test names of arguments match SimpleLoggingConfig API
        """
        parser = ArgumentParser(description="Test Program")
        add_logging_arguments(parser)
        args = parser.parse_args()
        args_dict = vars(args)
        assert "config" in args_dict
        assert "verbose" in args_dict
        assert "levels" in args_dict
        assert "modules" in args_dict
        assert "log_file_path" in args_dict
        assert "backup_count" in args_dict
