"""
Methods to support file handler related aspects of logging configuation.
"""

from pathlib import Path
import logging
import sys


logger = logging.getLogger(__name__)


def _get_log_file_name() -> str:
    """Use the name of the script for the log filename."""
    log_file_name = f"{Path(sys.argv[0]).stem}.log"
    logger.debug("Using module name for log file name: %s", log_file_name)
    return log_file_name


def _get_log_file(log_file_path: str) -> Path:
    """
    Return the absoulte path to use for the log file.
    log_file_path could be a path or filename.
    if log_file is an existing folder, then append the name of the calling module
    with a .log extension, and use this as the log file.
    """
    log_file = Path(log_file_path).resolve()
    if log_file.is_dir():
        return Path(log_file, _get_log_file_name())
    return log_file


def _set_log_file(config_data: dict, log_file: Path) -> bool:
    """Update the log file path in config."""
    if log_file:
        for data in config_data["handlers"].values():
            if "filename" in data:
                logger.debug("Setting log file path: %s", log_file)
                data["filename"] = str(log_file)
                return True
    return False


def _set_log_file_backup_count(config_data: dict, count: int) -> bool:
    """Set the backup count for a rotating file handler"""
    if count:
        for data in config_data["handlers"].values():
            if "backupCount" in data:
                logger.debug("Setting log file backup count: %s", count)
                data["backupCount"] = int(count)
                return True
    return False


def modify_log_file_attributes(
    config_data: dict, log_file_path: Path, backup_count: int
) -> None:
    """Set log file path and name and update backup count."""
    log_file = _get_log_file(log_file_path)
    _set_log_file(config_data, log_file)
    _set_log_file_backup_count(config_data, backup_count)


def rotate_log() -> None:
    """Rotate the log."""
    for handler in logging.getLogger().handlers:
        if hasattr(handler, "doRollover"):
            logger.debug("Rotating log")
            handler.doRollover()
