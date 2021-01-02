# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1StatefulSetStatus:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, collision_count: Optional[Any] = ..., conditions: Optional[Any] = ..., current_replicas: Optional[Any] = ..., current_revision: Optional[Any] = ..., observed_generation: Optional[Any] = ..., ready_replicas: Optional[Any] = ..., replicas: Optional[Any] = ..., update_revision: Optional[Any] = ..., updated_replicas: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def collision_count(self): ...
    @collision_count.setter
    def collision_count(self, collision_count: Any) -> None: ...
    @property
    def conditions(self): ...
    @conditions.setter
    def conditions(self, conditions: Any) -> None: ...
    @property
    def current_replicas(self): ...
    @current_replicas.setter
    def current_replicas(self, current_replicas: Any) -> None: ...
    @property
    def current_revision(self): ...
    @current_revision.setter
    def current_revision(self, current_revision: Any) -> None: ...
    @property
    def observed_generation(self): ...
    @observed_generation.setter
    def observed_generation(self, observed_generation: Any) -> None: ...
    @property
    def ready_replicas(self): ...
    @ready_replicas.setter
    def ready_replicas(self, ready_replicas: Any) -> None: ...
    @property
    def replicas(self): ...
    @replicas.setter
    def replicas(self, replicas: Any) -> None: ...
    @property
    def update_revision(self): ...
    @update_revision.setter
    def update_revision(self, update_revision: Any) -> None: ...
    @property
    def updated_replicas(self): ...
    @updated_replicas.setter
    def updated_replicas(self, updated_replicas: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
