# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1HorizontalPodAutoscalerListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1HorizontalPodAutoscalerDict, V1ListMetaDict

V1HorizontalPodAutoscalerListDict = TypedDict(
    "V1HorizontalPodAutoscalerListDict",
    {
        "apiVersion": str,
        "items": List[V1HorizontalPodAutoscalerDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)