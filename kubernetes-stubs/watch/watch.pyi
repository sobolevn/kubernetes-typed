# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes import client as client
from typing import Any

PYDOC_RETURN_LABEL: str
PYDOC_FOLLOW_PARAM: str
TYPE_LIST_SUFFIX: str
PY2: Any
HTTP_STATUS_GONE: Any

class SimpleNamespace:
    def __init__(self, **kwargs) -> None: ...

def iter_resp_lines(resp) -> None: ...

class Watch:
    resource_version: Any
    def __init__(self, return_type: Any | None = ...) -> None: ...
    def stop(self) -> None: ...
    def get_return_type(self, func): ...
    def get_watch_argument_name(self, func): ...
    def unmarshal_event(self, data, return_type): ...
    def stream(self, func, *args, **kwargs) -> None: ...