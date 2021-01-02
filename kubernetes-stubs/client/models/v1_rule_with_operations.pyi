# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1RuleWithOperations:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, api_groups: Optional[Any] = ..., api_versions: Optional[Any] = ..., operations: Optional[Any] = ..., resources: Optional[Any] = ..., scope: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def api_groups(self): ...
    @api_groups.setter
    def api_groups(self, api_groups: Any) -> None: ...
    @property
    def api_versions(self): ...
    @api_versions.setter
    def api_versions(self, api_versions: Any) -> None: ...
    @property
    def operations(self): ...
    @operations.setter
    def operations(self, operations: Any) -> None: ...
    @property
    def resources(self): ...
    @resources.setter
    def resources(self, resources: Any) -> None: ...
    @property
    def scope(self): ...
    @scope.setter
    def scope(self, scope: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
