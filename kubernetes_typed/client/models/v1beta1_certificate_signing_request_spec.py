# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1CertificateSigningRequestSpecDict generated type."""
from typing import TypedDict, Dict, List

V1beta1CertificateSigningRequestSpecDict = TypedDict(
    "V1beta1CertificateSigningRequestSpecDict",
    {
        "extra": Dict[str, List[str]],
        "groups": List[str],
        "request": str,
        "signerName": str,
        "uid": str,
        "usages": List[str],
        "username": str,
    },
    total=False,
)