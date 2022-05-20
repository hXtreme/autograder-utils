"""
Result builder class for Gradescope.
"""
import json

from dataclasses import asdict, dataclass, field, InitVar
from enum import Enum
from typing import List


class Visibility(str, Enum):
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

@dataclass
class Result:
    score: float = field(default=None)
    execution_time: float = field(default=None)
    output: str = field(default="")
    visibility: Visibility = Visibility.VISIBLE
    stdout_visibility: Visibility = Visibility.VISIBLE
    extra_data: dict = field(default_factory=dict)
    tests: List[Test] = field(default_factory=list)
    leaderboard: List[dict] = field(default=None)

    def __to_dict__(self):
        def clean(dt):
            if dt is None or dt == "":
                return None
            if isinstance(dt, dict):
                d = {}
                for k, v in dt.items():
                    v = clean(v)
                    if v is not None:
                        d[k] = clean(v)
                if len(d) == 0:
                    return None
                return d
            if isinstance(dt, list):
                d = []
                for v in dt:
                    v = clean(v)
                    if v is not None:
                        d.append(v)
                if len(d) == 0:
                    return None
                return d
            return dt
        dict_rep = clean(asdict(self))
        return dict_rep

    def dump(self, path: str = "results.json"):
        dict_rep = self.__to_dict__()
        with open(path, "w") as f:
            json.dump(dict_rep, f, indent=2)
