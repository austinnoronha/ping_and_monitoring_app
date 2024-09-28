"""Logger."""

import logging


def setup_logger(name: str):
    """Sets up a logger with the given name.

    Args:
        name (str): The name of the logger (usually the __name__ of the module).

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter("%(levelname)s:  %(asctime)s \t %(name)s \t %(message)s")
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    if not logger.handlers:
        logger.addHandler(ch)

    return logger
