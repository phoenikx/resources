import logging

import coloredlogs


def get_logger():
    logger = logging.getLogger('resources')
    logger.setLevel(logging.INFO)
    coloredlogs.install(level='INFO', logger=logger, fmt="%(msg)s")
    return logger
