# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1JobListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1JobDict, V1ListMetaDict

V1JobListDict = TypedDict(
    "V1JobListDict",
    {
        "apiVersion": str,
        "items": List[V1JobDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)