# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1NodeDaemonEndpointsDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1DaemonEndpointDict

V1NodeDaemonEndpointsDict = TypedDict(
    "V1NodeDaemonEndpointsDict",
    {
        "kubeletEndpoint": V1DaemonEndpointDict,
    },
    total=False,
)