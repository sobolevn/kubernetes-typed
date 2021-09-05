# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta2HorizontalPodAutoscalerSpecDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V2beta2CrossVersionObjectReferenceDict, V2beta2HorizontalPodAutoscalerBehaviorDict, V2beta2MetricSpecDict

V2beta2HorizontalPodAutoscalerSpecDict = TypedDict(
    "V2beta2HorizontalPodAutoscalerSpecDict",
    {
        "behavior": V2beta2HorizontalPodAutoscalerBehaviorDict,
        "maxReplicas": int,
        "metrics": List[V2beta2MetricSpecDict],
        "minReplicas": int,
        "scaleTargetRef": V2beta2CrossVersionObjectReferenceDict,
    },
    total=False,
)