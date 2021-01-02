# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any, Optional

class DiscoveryV1alpha1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def create_namespaced_endpoint_slice(self, namespace: Any, body: Any, **kwargs: Any): ...
    def create_namespaced_endpoint_slice_with_http_info(self, namespace: Any, body: Any, **kwargs: Any): ...
    def delete_collection_namespaced_endpoint_slice(self, namespace: Any, **kwargs: Any): ...
    def delete_collection_namespaced_endpoint_slice_with_http_info(self, namespace: Any, **kwargs: Any): ...
    def delete_namespaced_endpoint_slice(self, name: Any, namespace: Any, **kwargs: Any): ...
    def delete_namespaced_endpoint_slice_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def get_api_resources(self, **kwargs: Any): ...
    def get_api_resources_with_http_info(self, **kwargs: Any): ...
    def list_endpoint_slice_for_all_namespaces(self, **kwargs: Any): ...
    def list_endpoint_slice_for_all_namespaces_with_http_info(self, **kwargs: Any): ...
    def list_namespaced_endpoint_slice(self, namespace: Any, **kwargs: Any): ...
    def list_namespaced_endpoint_slice_with_http_info(self, namespace: Any, **kwargs: Any): ...
    def patch_namespaced_endpoint_slice(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_endpoint_slice_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def read_namespaced_endpoint_slice(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_endpoint_slice_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def replace_namespaced_endpoint_slice(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_endpoint_slice_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
