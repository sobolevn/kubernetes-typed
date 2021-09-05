# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1SubjectAccessReviewSpecDict generated type."""
from typing import TypedDict, Dict, List

from kubernetes_typed.client import V1beta1NonResourceAttributesDict, V1beta1ResourceAttributesDict

V1beta1SubjectAccessReviewSpecDict = TypedDict(
    "V1beta1SubjectAccessReviewSpecDict",
    {
        "extra": Dict[str, List[str]],
        "group": List[str],
        "nonResourceAttributes": V1beta1NonResourceAttributesDict,
        "resourceAttributes": V1beta1ResourceAttributesDict,
        "uid": str,
        "user": str,
    },
    total=False,
)