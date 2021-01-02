# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta2DeploymentSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, min_ready_seconds: Optional[Any] = ..., paused: Optional[Any] = ..., progress_deadline_seconds: Optional[Any] = ..., replicas: Optional[Any] = ..., revision_history_limit: Optional[Any] = ..., selector: Optional[Any] = ..., strategy: Optional[Any] = ..., template: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def min_ready_seconds(self): ...
    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds: Any) -> None: ...
    @property
    def paused(self): ...
    @paused.setter
    def paused(self, paused: Any) -> None: ...
    @property
    def progress_deadline_seconds(self): ...
    @progress_deadline_seconds.setter
    def progress_deadline_seconds(self, progress_deadline_seconds: Any) -> None: ...
    @property
    def replicas(self): ...
    @replicas.setter
    def replicas(self, replicas: Any) -> None: ...
    @property
    def revision_history_limit(self): ...
    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit: Any) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector: Any) -> None: ...
    @property
    def strategy(self): ...
    @strategy.setter
    def strategy(self, strategy: Any) -> None: ...
    @property
    def template(self): ...
    @template.setter
    def template(self, template: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
