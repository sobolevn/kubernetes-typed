# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1CustomResourceDefinitionSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, additional_printer_columns: Optional[Any] = ..., conversion: Optional[Any] = ..., group: Optional[Any] = ..., names: Optional[Any] = ..., preserve_unknown_fields: Optional[Any] = ..., scope: Optional[Any] = ..., subresources: Optional[Any] = ..., validation: Optional[Any] = ..., version: Optional[Any] = ..., versions: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def additional_printer_columns(self): ...
    @additional_printer_columns.setter
    def additional_printer_columns(self, additional_printer_columns: Any) -> None: ...
    @property
    def conversion(self): ...
    @conversion.setter
    def conversion(self, conversion: Any) -> None: ...
    @property
    def group(self): ...
    @group.setter
    def group(self, group: Any) -> None: ...
    @property
    def names(self): ...
    @names.setter
    def names(self, names: Any) -> None: ...
    @property
    def preserve_unknown_fields(self): ...
    @preserve_unknown_fields.setter
    def preserve_unknown_fields(self, preserve_unknown_fields: Any) -> None: ...
    @property
    def scope(self): ...
    @scope.setter
    def scope(self, scope: Any) -> None: ...
    @property
    def subresources(self): ...
    @subresources.setter
    def subresources(self, subresources: Any) -> None: ...
    @property
    def validation(self): ...
    @validation.setter
    def validation(self, validation: Any) -> None: ...
    @property
    def version(self): ...
    @version.setter
    def version(self, version: Any) -> None: ...
    @property
    def versions(self): ...
    @versions.setter
    def versions(self, versions: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
