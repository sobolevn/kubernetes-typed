# Code generated by `typeddictgen`. DO NOT EDIT.
"""NetworkingV1beta1IngressBackendDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1TypedLocalObjectReferenceDict

NetworkingV1beta1IngressBackendDict = TypedDict(
    "NetworkingV1beta1IngressBackendDict",
    {
        "resource": V1TypedLocalObjectReferenceDict,
        "serviceName": str,
        "servicePort": object,
    },
    total=False,
)