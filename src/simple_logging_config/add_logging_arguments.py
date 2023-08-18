"""
Add arguments to a parser to support logging features
"""


from ._logging_config import read_configs

def add_logging_arguments(parser):
    """
    Add logging argumnets to parser to support logging
    """
    configs = read_configs().keys()
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="count",
        default=0,
        help=(
            "The level of logging verbosity for the default handler. "
            "Use multiple times (up to -vvv) for increased verbosity."
        ),
    )
    group.add_argument(
        "--slc_levels",
        dest="slc_levels",
        nargs="*",
        type=str,
        help=(
            "The log levels to be applied to attached handlers. The "
            "levels are applied to the handlers in the order the handlers "
            "are registered. To skip a handler, use 'None' or '-'."
        ),
    )
    parser.add_argument(
        "--slc_modules",
        dest="slc_modules",
        nargs="*",
        type=str,
        help=(
            "The names of the modules to be logged. If omitted all modules "
            "are logged."
        ),
    )
    parser.add_argument(
        "--slc_log_file_path",
        dest="slc_log_file_path",
        type=str,
        help=(
            "The path the log file will be saved to. If this is a folder, "
            "the log file will be saved to this folder with the file name "
            "derived from the name of the calling script. Otherwise, assume "
            "this is a full path to a named log file."
        ),
    )
    parser.add_argument(
        "--slc_backup_count",
        dest="slc_backup_count",
        default=0,
        type=int,
        help=("An integer specifying The number of backup log files to retain."),
    )
    parser.add_argument(
        "--slc_config",
        dest="slc_config",
        choices=configs,
        type=str,
        help="The name of the logging config to be used.",
    )
