from typing import Literal, TypedDict

class Action(TypedDict):
    type: Literal["browser", "shell", "none"]
    target: str