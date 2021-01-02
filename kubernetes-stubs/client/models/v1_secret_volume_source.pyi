# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1SecretVolumeSource:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, default_mode: Optional[Any] = ..., items: Optional[Any] = ..., optional: Optional[Any] = ..., secret_name: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def default_mode(self): ...
    @default_mode.setter
    def default_mode(self, default_mode: Any) -> None: ...
    @property
    def items(self): ...
    @items.setter
    def items(self, items: Any) -> None: ...
    @property
    def optional(self): ...
    @optional.setter
    def optional(self, optional: Any) -> None: ...
    @property
    def secret_name(self): ...
    @secret_name.setter
    def secret_name(self, secret_name: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
