# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1ClientIPConfig:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, timeout_seconds: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def timeout_seconds(self): ...
    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
