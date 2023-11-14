"""
Test support for logging to file functions.

99% tested by default configuration
"""

from os import makedirs, listdir
from pathlib import Path
import logging

from simple_logging_config import configure_logging


LOGS_FOLDER = "logs"


class TestLogFileSettings:
    """
    Class to test log to file functions
    """

    def test_log_file_path_as_filename(self):
        """
        Test log file path can be set as a file name
        """
        log_file_path_as_filename = "test_as_filename.log"
        configure_logging(log_file_path=log_file_path_as_filename)
        assert Path(log_file_path_as_filename).is_file()

    def test_log_file_path_as_path(self):
        """
        Test log file path can be set as a folder
        """
        log_file_path_as_path = LOGS_FOLDER
        makedirs(Path(log_file_path_as_path), exist_ok=True)
        configure_logging(log_file_path=log_file_path_as_path)
        assert Path(log_file_path_as_path).is_dir()

    def test_rotating_limits_to_5_backups(self):
        """
        Test rotating handler creates 5 backups
        """
        log_file_path_as_path = LOGS_FOLDER
        backup_count = 5  # default
        makedirs(Path(log_file_path_as_path), exist_ok=True)
        slc = configure_logging(config="rotating_file", log_file_path=log_file_path_as_path)
        logger = logging.getLogger(__name__)
        loop = backup_count + 2  # Rotate more than backups expected
        expected = backup_count + 1  # Backups = Numbered backups + current
        for i in range(0, loop):
            logger.debug("Rotation #%s", i)
            slc.rotate()
        backup_file_count = len(listdir(log_file_path_as_path))
        assert backup_file_count == expected

    def test_setting_numbr_of_backup_files(self):
        """
        Test setting number of backup files
        """
        log_file_path_as_path = LOGS_FOLDER
        backup_count = 3
        makedirs(Path(log_file_path_as_path), exist_ok=True)
        slc = configure_logging(
            config="rotating_file",
            backup_count=backup_count,
            log_file_path=log_file_path_as_path,
        )
        logger = logging.getLogger(__name__)
        loop = backup_count + 2  # Rotate more than backups expected
        expected = backup_count + 1  # Backups = Numbered backups + current
        for i in range(0, loop):
            logger.debug("Rotation #%s", i)
            slc.rotate()
        backup_file_count = len(listdir(log_file_path_as_path))
        assert backup_file_count == expected
