"""
Test ArgumentParser logging arguments
"""

from argparse import ArgumentParser
import logging

from simple_logging_config import add_logging_arguments


logger = logging.getLogger(__name__)


class TestArguments:
    """
    Class to test default config .
    """

    def test_arguments(self):
        """
        Test names of arguments match SimpleLoggingConfig API
        """
        parser = ArgumentParser(description="Test Program")
        add_logging_arguments(parser)
        # Must use parse_known_args() as parser includes pytest args
        args, _ = parser.parse_known_args()
        assert args.config is None
        assert args.verbose == 0
        assert args.levels is None
        assert args.modules is None
        assert args.log_file_path is None
        assert args.backup_count is None
