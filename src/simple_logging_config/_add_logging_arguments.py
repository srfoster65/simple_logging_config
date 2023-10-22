"""
Add arguments to a parser to support logging features
"""


from ._logging_config import read_configs

def add_logging_arguments(parser):
    """
    Add logging argumnets to parser to enable configuring logging
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
        "--slc-level", "--slc-levels",
        dest="levels",
        type=str,
        help=(
            "The log level(s) to be applied to attached handlers. "
            "This value can be a single integer or a string representing a "
            "defined log level. Or it can be a string representing a dictionary "
            "where key/value pairs are handler names and the log level to be "
            "associated with that handler"
        ),
    )
    parser.add_argument(
        "--slc-modules",
        dest="modules",
        nargs="*",
        type=str,
        help=(
            "The names of the modules to be logged. If omitted all modules "
            "are logged."
        ),
    )
    parser.add_argument(
        "--slc-log-file-path",
        dest="log_file_path",
        type=str,
        help=(
            "The path the log file will be saved to. If this is a folder, "
            "the log file will be saved to this folder with the file name "
            "derived from the name of the calling script. Otherwise, assume "
            "this is a full path to a named log file."
        ),
    )
    parser.add_argument(
        "--slc-backup-count",
        dest="backup_count",
        type=int,
        help=("An integer specifying The number of backup log files to retain."),
    )
    parser.add_argument(
        "--slc-config",
        dest="config",
        choices=configs,
        type=str,
        help="The name of the logging config to be used.",
    )
