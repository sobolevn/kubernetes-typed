# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1AzureFilePersistentVolumeSourceDict generated type."""
from typing import TypedDict

V1AzureFilePersistentVolumeSourceDict = TypedDict(
    "V1AzureFilePersistentVolumeSourceDict",
    {
        "readOnly": bool,
        "secretName": str,
        "secretNamespace": str,
        "shareName": str,
    },
    total=False,
)