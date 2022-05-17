"""Utilities to build a project"""

import os
import subprocess

import agu.ctx as ctx

from subprocess import PIPE, CompletedProcess


def cmake(build_dir="./build", run_make=True, clean=False) -> None:
    """
    Build a project with cmake.

    :param build_dir: The directory to build the project in.
    :param run_make: Run make after cmake?
    :param clean: Clean the build directory before building?
    :throws: subprocess.CalledProcessError if the build fails.
    """
    if clean:
        os.system(f"rm -rf {build_dir}")
        os.system(f"mkdir -p {build_dir}")
    with ctx.pushd(build_dir):
        cmake_process = subprocess.run(
            ["cmake", ".."],
            stdout=PIPE,
            stderr=PIPE,
            universal_newlines=True,
            check=True,
        )
        assert cmake_process.returncode == 0
        if run_make:
            make()


def make(target=None, clean=False) -> CompletedProcess:
    """
    Build a project with make.

    :param target: make target.
    :param clean: clean build the project?
    :throws: subprocess.CalledProcessError if the build fails.
    """
    target = list() if target is None else [target]
    if clean:
        target = ["clean"] + target
    print(f"Building with make in {os.getcwd()}")
    make_process = subprocess.run(
        ["make"] + target,
        stdout=PIPE,
        stderr=PIPE,
        universal_newlines=True,
        check=True,
    )
    assert make_process.returncode == 0
    return make_process
