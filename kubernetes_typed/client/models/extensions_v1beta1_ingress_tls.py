# Code generated by `typeddictgen`. DO NOT EDIT.
"""ExtensionsV1beta1IngressTLSDict generated type."""
from typing import TypedDict, List

ExtensionsV1beta1IngressTLSDict = TypedDict(
    "ExtensionsV1beta1IngressTLSDict",
    {
        "hosts": List[str],
        "secretName": str,
    },
    total=False,
)