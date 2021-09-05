# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1PodSecurityContextDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1SELinuxOptionsDict, V1SysctlDict, V1WindowsSecurityContextOptionsDict

V1PodSecurityContextDict = TypedDict(
    "V1PodSecurityContextDict",
    {
        "fsGroup": int,
        "fsGroupChangePolicy": str,
        "runAsGroup": int,
        "runAsNonRoot": bool,
        "runAsUser": int,
        "seLinuxOptions": V1SELinuxOptionsDict,
        "supplementalGroups": List[int],
        "sysctls": List[V1SysctlDict],
        "windowsOptions": V1WindowsSecurityContextOptionsDict,
    },
    total=False,
)