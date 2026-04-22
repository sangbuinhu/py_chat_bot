"""Console output utilities with ANSI color support."""

from datetime import datetime


class BColors:
    """ANSI color codes for terminal output."""

    WARNING = "\033[93m"
    ENDC = "\033[0m"
    CRED = "\33[31m"
    CBLUE = "\33[34m"


def warning(message):
    """Print a yellow warning message."""
    print(f"{BColors.WARNING}WARNING: {message}{BColors.ENDC}", flush=True)


def info(message):
    """Print a blue info message."""
    print(f"{BColors.CBLUE}INFO: {message}{BColors.ENDC}", flush=True)


def logger(file_name: str, function: str, message: str):
    """Print a red error log with file, function, message, and timestamp."""
    print(f"{BColors.CRED}FILE: {file_name}{BColors.ENDC}", flush=True)
    print(f"{BColors.CRED}FUNCTION: {function}{BColors.ENDC}", flush=True)
    print(f"{BColors.CRED}ERROR: {message}{BColors.ENDC}", flush=True)
    print(
        f"{BColors.CRED}TIME: {datetime.now().strftime('%Y/%m/%d %H:%M:%S')}{BColors.ENDC}",
        flush=True,
    )
