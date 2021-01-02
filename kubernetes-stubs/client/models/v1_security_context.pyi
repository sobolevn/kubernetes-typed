# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1SecurityContext:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, allow_privilege_escalation: Optional[Any] = ..., capabilities: Optional[Any] = ..., privileged: Optional[Any] = ..., proc_mount: Optional[Any] = ..., read_only_root_filesystem: Optional[Any] = ..., run_as_group: Optional[Any] = ..., run_as_non_root: Optional[Any] = ..., run_as_user: Optional[Any] = ..., se_linux_options: Optional[Any] = ..., windows_options: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def allow_privilege_escalation(self): ...
    @allow_privilege_escalation.setter
    def allow_privilege_escalation(self, allow_privilege_escalation: Any) -> None: ...
    @property
    def capabilities(self): ...
    @capabilities.setter
    def capabilities(self, capabilities: Any) -> None: ...
    @property
    def privileged(self): ...
    @privileged.setter
    def privileged(self, privileged: Any) -> None: ...
    @property
    def proc_mount(self): ...
    @proc_mount.setter
    def proc_mount(self, proc_mount: Any) -> None: ...
    @property
    def read_only_root_filesystem(self): ...
    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, read_only_root_filesystem: Any) -> None: ...
    @property
    def run_as_group(self): ...
    @run_as_group.setter
    def run_as_group(self, run_as_group: Any) -> None: ...
    @property
    def run_as_non_root(self): ...
    @run_as_non_root.setter
    def run_as_non_root(self, run_as_non_root: Any) -> None: ...
    @property
    def run_as_user(self): ...
    @run_as_user.setter
    def run_as_user(self, run_as_user: Any) -> None: ...
    @property
    def se_linux_options(self): ...
    @se_linux_options.setter
    def se_linux_options(self, se_linux_options: Any) -> None: ...
    @property
    def windows_options(self): ...
    @windows_options.setter
    def windows_options(self, windows_options: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...