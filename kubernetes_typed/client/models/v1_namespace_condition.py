# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1NamespaceConditionDict generated type."""
import datetime
from typing import TypedDict

V1NamespaceConditionDict = TypedDict(
    "V1NamespaceConditionDict",
    {
        "lastTransitionTime": datetime.datetime,
        "message": str,
        "reason": str,
        "status": str,
        "type": str,
    },
    total=False,
)