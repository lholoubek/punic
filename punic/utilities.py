from __future__ import division, absolute_import, print_function

__all__ = ['work_directory', 'timeit']

import contextlib
import os
import time
from .logger import *


@contextlib.contextmanager
def work_directory(path):
    # type: (Union[Path, None])
    saved_wd = None
    if path:
        path = str(path)
        saved_wd = os.getcwd()
        os.chdir(path)
    try:
        yield
    except:
        raise
    finally:
        if saved_wd:
            os.chdir(saved_wd)


@contextlib.contextmanager
def timeit(task=None):
    # type: (Union[str, None])
    start = time.time()
    yield
    end = time.time()
    logger.debug('Task \'<ref>{}</ref>\' took <echo>{:.6f}</echo> seconds.'.format(task if task else '<unnamed task>',
        end - start))
