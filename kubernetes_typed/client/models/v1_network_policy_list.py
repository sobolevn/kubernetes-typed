# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1NetworkPolicyListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1NetworkPolicyDict

V1NetworkPolicyListDict = TypedDict(
    "V1NetworkPolicyListDict",
    {
        "apiVersion": str,
        "items": List[V1NetworkPolicyDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)