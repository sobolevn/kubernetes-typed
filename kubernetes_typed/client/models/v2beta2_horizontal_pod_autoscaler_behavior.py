# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta2HorizontalPodAutoscalerBehaviorDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V2beta2HPAScalingRulesDict

V2beta2HorizontalPodAutoscalerBehaviorDict = TypedDict(
    "V2beta2HorizontalPodAutoscalerBehaviorDict",
    {
        "scaleDown": V2beta2HPAScalingRulesDict,
        "scaleUp": V2beta2HPAScalingRulesDict,
    },
    total=False,
)