# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1RoleListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1RoleDict

V1RoleListDict = TypedDict(
    "V1RoleListDict",
    {
        "apiVersion": str,
        "items": List[V1RoleDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)