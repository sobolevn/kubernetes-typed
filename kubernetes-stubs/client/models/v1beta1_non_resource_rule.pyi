# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1NonResourceRule:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, non_resource_ur_ls: Optional[Any] = ..., verbs: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def non_resource_ur_ls(self): ...
    @non_resource_ur_ls.setter
    def non_resource_ur_ls(self, non_resource_ur_ls: Any) -> None: ...
    @property
    def verbs(self): ...
    @verbs.setter
    def verbs(self, verbs: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
