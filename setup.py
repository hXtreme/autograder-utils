from os import path

from setuptools import setup, find_packages

BASE_PATH = path.dirname(path.abspath(__file__))

with open(f"{BASE_PATH}/requirements.txt", "r") as fp:
    requirements = fp.read().splitlines()

setup(
    name="autograder-utils",
    author="Harsh Parekh",
    author_email="harsh_parekh@outlook.com",
    url="https://git.parekh.page/autograder-utils",
    python_requires=">=3.6",
    description="A library of python functions to make building autograder simpler.",
    license="MIT",
    packages=find_packages(include=["agu", "agu.*"]),
    install_requires=requirements,
)
