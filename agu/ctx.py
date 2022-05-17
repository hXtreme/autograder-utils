"""Contexts that make it easier to build a autograder."""

import os
import contextlib


@contextlib.contextmanager
def pushd(newdir):
    """Context manager to go into a directory and return back when done."""
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)
