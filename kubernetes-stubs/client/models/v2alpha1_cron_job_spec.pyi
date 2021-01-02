# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V2alpha1CronJobSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, concurrency_policy: Optional[Any] = ..., failed_jobs_history_limit: Optional[Any] = ..., job_template: Optional[Any] = ..., schedule: Optional[Any] = ..., starting_deadline_seconds: Optional[Any] = ..., successful_jobs_history_limit: Optional[Any] = ..., suspend: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def concurrency_policy(self): ...
    @concurrency_policy.setter
    def concurrency_policy(self, concurrency_policy: Any) -> None: ...
    @property
    def failed_jobs_history_limit(self): ...
    @failed_jobs_history_limit.setter
    def failed_jobs_history_limit(self, failed_jobs_history_limit: Any) -> None: ...
    @property
    def job_template(self): ...
    @job_template.setter
    def job_template(self, job_template: Any) -> None: ...
    @property
    def schedule(self): ...
    @schedule.setter
    def schedule(self, schedule: Any) -> None: ...
    @property
    def starting_deadline_seconds(self): ...
    @starting_deadline_seconds.setter
    def starting_deadline_seconds(self, starting_deadline_seconds: Any) -> None: ...
    @property
    def successful_jobs_history_limit(self): ...
    @successful_jobs_history_limit.setter
    def successful_jobs_history_limit(self, successful_jobs_history_limit: Any) -> None: ...
    @property
    def suspend(self): ...
    @suspend.setter
    def suspend(self, suspend: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
