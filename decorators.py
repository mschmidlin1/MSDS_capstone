import functools
import logging
from configs import set_logger
set_logger()













#logging decorators
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logging.debug(f"Running function {func.__name__}")
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logging.error(f"Exception raised in {func.__name__}. exception: {str(e)}")
            raise e
    return wrapper





