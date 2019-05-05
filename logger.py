import logging
import os
import sys

log_levels = {
    "critical": logging.CRITICAL,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "info": logging.INFO,
    "debug": logging.DEBUG,
}


def configure_logger(logger_config):
    params = {
        "stream": sys.stderr,
        "level": log_levels.get(logger_config["level"], logging.INFO),
        "format": "%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",
        "datefmt": "%Y-%m-%d %X",
        "filemode": "w",
    }

    if logger_config:
        logdir = logger_config.get("logdir", ".")
        log_file_name = logger_config.get("log_file_name")
        if log_file_name:
            params["filename"] = os.path.join(logdir, log_file_name)
            del params["stream"]

    logging.basicConfig(**params)

    return logging
