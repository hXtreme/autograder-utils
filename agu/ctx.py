"""Contexts that make it easier to build a autograder."""

import os
import contextlib


@contextlib.contextmanager
def pushd(newdir):
    """Context manager to go into a directory and return back when done."""
    prevdir, newdir = os.getcwd(), os.path.expanduser(newdir)
    os.chdir(newdir)
    try:
        yield newdir
    finally:
        os.chdir(prevdir)
