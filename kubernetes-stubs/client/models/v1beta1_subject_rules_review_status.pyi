# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1SubjectRulesReviewStatus:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, evaluation_error: Optional[Any] = ..., incomplete: Optional[Any] = ..., non_resource_rules: Optional[Any] = ..., resource_rules: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def evaluation_error(self): ...
    @evaluation_error.setter
    def evaluation_error(self, evaluation_error: Any) -> None: ...
    @property
    def incomplete(self): ...
    @incomplete.setter
    def incomplete(self, incomplete: Any) -> None: ...
    @property
    def non_resource_rules(self): ...
    @non_resource_rules.setter
    def non_resource_rules(self, non_resource_rules: Any) -> None: ...
    @property
    def resource_rules(self): ...
    @resource_rules.setter
    def resource_rules(self, resource_rules: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
