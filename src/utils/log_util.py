"""Logging utilities for formatted error output."""

import traceback

from src.utils import console


def show_log(error: Exception) -> None:
    """Log an exception with file, function, and message details.

    Parses the current traceback to extract the source file and function name,
    then delegates to console.logger for colored output.

    Args:
        error: The exception to log.
    """
    formatted_lines = traceback.format_exc().splitlines()
    if len(formatted_lines) > 1:
        e = formatted_lines[1].strip().split(",")
        file_name = (
            (e[0] + e[1]).replace("File", "").strip()
            if len(e) > 1
            else e[0].replace("File", "").strip()
        )
        function = e[-1].replace(" in", "").strip()
    else:
        tb = traceback.extract_stack()
        frame = tb[-2] if len(tb) >= 2 else tb[-1]
        file_name = frame.filename
        function = frame.name
    console.logger(
        file_name=file_name,
        function=function,
        message=str(error),
    )
