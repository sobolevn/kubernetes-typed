# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1PriorityClass:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, api_version: Optional[Any] = ..., description: Optional[Any] = ..., global_default: Optional[Any] = ..., kind: Optional[Any] = ..., metadata: Optional[Any] = ..., preemption_policy: Optional[Any] = ..., value: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version: Any) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description: Any) -> None: ...
    @property
    def global_default(self): ...
    @global_default.setter
    def global_default(self, global_default: Any) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind: Any) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, metadata: Any) -> None: ...
    @property
    def preemption_policy(self): ...
    @preemption_policy.setter
    def preemption_policy(self, preemption_policy: Any) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
