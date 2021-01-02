# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1VsphereVirtualDiskVolumeSource:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, fs_type: Optional[Any] = ..., storage_policy_id: Optional[Any] = ..., storage_policy_name: Optional[Any] = ..., volume_path: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def fs_type(self): ...
    @fs_type.setter
    def fs_type(self, fs_type: Any) -> None: ...
    @property
    def storage_policy_id(self): ...
    @storage_policy_id.setter
    def storage_policy_id(self, storage_policy_id: Any) -> None: ...
    @property
    def storage_policy_name(self): ...
    @storage_policy_name.setter
    def storage_policy_name(self, storage_policy_name: Any) -> None: ...
    @property
    def volume_path(self): ...
    @volume_path.setter
    def volume_path(self, volume_path: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...