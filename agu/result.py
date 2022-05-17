"""
Result builder class for Gradescope.
"""
import json

from dataclasses import asdict, dataclass, field, InitVar
from enum import Enum
from typing import Any


class Visibility(Enum):
    """
    Enum for visibility.
    """

    HIDDEN = "hidden"
    AFTER_DUE_DATE = "after_due_date"
    AFTER_PUBLISHED = "after_published"
    VISIBLE = "visible"


@dataclass
class Test:
    score: float = field(default=None)
    max_score: float = field(default=None)
    name: str = field(default=None)
    number_major: InitVar[int] = None
    number_minor: InitVar[int] = None
    output: str = field(default="")
    tags: list = field(default_factory=list)
    visibility: Visibility = Visibility.VISIBLE
    extra_data: dict = field(default_factory=dict)
    number: str = field(init=False)

    def __post_init__(self, number_major, number_minor):
        self.number = None
        if self.number_major is not None:
            self.number_major = f"{number_major}"
        if self.number_minor is not None:
            self.number_minor += (
                "." if self.number is not None else ""
            ) + f"{number_minor}"


class Result:
    def __init__(
        self,
        visibility: Visibility = None,
        stdout_visibility: Visibility = None,
        **kwargs,
    ):
        self.__json = {}
        self.tests = []
        if visibility is not None:
            self.__json["visibility"] = visibility
        if stdout_visibility is not None:
            self.__json["stdout_visibility"] = stdout_visibility
        self.__json.update(kwargs)

    def add_test(self, test: Test):
        self.tests.append(test)
        return self

    def dump(self, path: str = "results.json"):
        _json = self.__json.copy()
        _json["tests"] = list(map(asdict, self.tests))
        with open(path, "w") as f:
            json.dump(self.__json, f, indent=2)

    def __setattr__(self, __name: str, __value: Any):
        self.__json[__name] = __value
        return self
