# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1ClusterRoleDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1ObjectMetaDict, V1beta1AggregationRuleDict, V1beta1PolicyRuleDict

V1beta1ClusterRoleDict = TypedDict(
    "V1beta1ClusterRoleDict",
    {
        "aggregationRule": V1beta1AggregationRuleDict,
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "rules": List[V1beta1PolicyRuleDict],
    },
    total=False,
)