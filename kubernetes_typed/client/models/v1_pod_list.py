# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1PodListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1PodDict

V1PodListDict = TypedDict(
    "V1PodListDict",
    {
        "apiVersion": str,
        "items": List[V1PodDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)