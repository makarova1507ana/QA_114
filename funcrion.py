import logging

logger = logging.getLogger(__name__)

def func():
    logger.info("start func()")
    print("func()")
    logger.info("end func()")