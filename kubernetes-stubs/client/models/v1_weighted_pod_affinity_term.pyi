# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1WeightedPodAffinityTerm:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, pod_affinity_term: Optional[Any] = ..., weight: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def pod_affinity_term(self): ...
    @pod_affinity_term.setter
    def pod_affinity_term(self, pod_affinity_term: Any) -> None: ...
    @property
    def weight(self): ...
    @weight.setter
    def weight(self, weight: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...