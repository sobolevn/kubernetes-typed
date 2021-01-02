# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any, Optional

class ApiextensionsV1beta1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def create_custom_resource_definition(self, body: Any, **kwargs: Any): ...
    def create_custom_resource_definition_with_http_info(self, body: Any, **kwargs: Any): ...
    def delete_collection_custom_resource_definition(self, **kwargs: Any): ...
    def delete_collection_custom_resource_definition_with_http_info(self, **kwargs: Any): ...
    def delete_custom_resource_definition(self, name: Any, **kwargs: Any): ...
    def delete_custom_resource_definition_with_http_info(self, name: Any, **kwargs: Any): ...
    def get_api_resources(self, **kwargs: Any): ...
    def get_api_resources_with_http_info(self, **kwargs: Any): ...
    def list_custom_resource_definition(self, **kwargs: Any): ...
    def list_custom_resource_definition_with_http_info(self, **kwargs: Any): ...
    def patch_custom_resource_definition(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_custom_resource_definition_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_custom_resource_definition_status(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_custom_resource_definition_status_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def read_custom_resource_definition(self, name: Any, **kwargs: Any): ...
    def read_custom_resource_definition_with_http_info(self, name: Any, **kwargs: Any): ...
    def read_custom_resource_definition_status(self, name: Any, **kwargs: Any): ...
    def read_custom_resource_definition_status_with_http_info(self, name: Any, **kwargs: Any): ...
    def replace_custom_resource_definition(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_custom_resource_definition_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_custom_resource_definition_status(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_custom_resource_definition_status_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
