# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any

class V1beta1HostPortRange:
    openapi_types: Any
    attribute_map: Any
    local_vars_configuration: Any
    discriminator: Any
    def __init__(self, max: Any | None = ..., min: Any | None = ..., local_vars_configuration: Any | None = ...) -> None: ...
    @property
    def max(self): ...
    @max.setter
    def max(self, max) -> None: ...
    @property
    def min(self): ...
    @min.setter
    def min(self, min) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...