import logging
import time
from functools import wraps


class TimerContextManager(object):
    """
    Context Manager to function/method execution time.

    Reason: try/finally antipattern.
    """

    def __init__(self, fname):
        """Init timer object (not stateless)."""
        self.t0 = time.perf_counter()
        self.fname = fname
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO,)

    def __enter__(self):
        """Pre-try: manager magic-method."""

    def __exit__(self, *args):
        """Finally: context manager magic-method."""
        elapsed = time.perf_counter() - self.t0
        logging.info('@Timer| [{0:02f}] {1}'.format(elapsed, self.fname))


def timer(func):
    """Measure how much time we spent executing function."""
    @wraps(func)
    def decorator(*args, **kwargs):
        with TimerContextManager(func.__name__):
            return func(*args, **kwargs)
    return decorator
