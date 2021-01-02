# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1PodSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, active_deadline_seconds: Optional[Any] = ..., affinity: Optional[Any] = ..., automount_service_account_token: Optional[Any] = ..., containers: Optional[Any] = ..., dns_config: Optional[Any] = ..., dns_policy: Optional[Any] = ..., enable_service_links: Optional[Any] = ..., ephemeral_containers: Optional[Any] = ..., host_aliases: Optional[Any] = ..., host_ipc: Optional[Any] = ..., host_network: Optional[Any] = ..., host_pid: Optional[Any] = ..., hostname: Optional[Any] = ..., image_pull_secrets: Optional[Any] = ..., init_containers: Optional[Any] = ..., node_name: Optional[Any] = ..., node_selector: Optional[Any] = ..., overhead: Optional[Any] = ..., preemption_policy: Optional[Any] = ..., priority: Optional[Any] = ..., priority_class_name: Optional[Any] = ..., readiness_gates: Optional[Any] = ..., restart_policy: Optional[Any] = ..., runtime_class_name: Optional[Any] = ..., scheduler_name: Optional[Any] = ..., security_context: Optional[Any] = ..., service_account: Optional[Any] = ..., service_account_name: Optional[Any] = ..., share_process_namespace: Optional[Any] = ..., subdomain: Optional[Any] = ..., termination_grace_period_seconds: Optional[Any] = ..., tolerations: Optional[Any] = ..., topology_spread_constraints: Optional[Any] = ..., volumes: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def active_deadline_seconds(self): ...
    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds: Any) -> None: ...
    @property
    def affinity(self): ...
    @affinity.setter
    def affinity(self, affinity: Any) -> None: ...
    @property
    def automount_service_account_token(self): ...
    @automount_service_account_token.setter
    def automount_service_account_token(self, automount_service_account_token: Any) -> None: ...
    @property
    def containers(self): ...
    @containers.setter
    def containers(self, containers: Any) -> None: ...
    @property
    def dns_config(self): ...
    @dns_config.setter
    def dns_config(self, dns_config: Any) -> None: ...
    @property
    def dns_policy(self): ...
    @dns_policy.setter
    def dns_policy(self, dns_policy: Any) -> None: ...
    @property
    def enable_service_links(self): ...
    @enable_service_links.setter
    def enable_service_links(self, enable_service_links: Any) -> None: ...
    @property
    def ephemeral_containers(self): ...
    @ephemeral_containers.setter
    def ephemeral_containers(self, ephemeral_containers: Any) -> None: ...
    @property
    def host_aliases(self): ...
    @host_aliases.setter
    def host_aliases(self, host_aliases: Any) -> None: ...
    @property
    def host_ipc(self): ...
    @host_ipc.setter
    def host_ipc(self, host_ipc: Any) -> None: ...
    @property
    def host_network(self): ...
    @host_network.setter
    def host_network(self, host_network: Any) -> None: ...
    @property
    def host_pid(self): ...
    @host_pid.setter
    def host_pid(self, host_pid: Any) -> None: ...
    @property
    def hostname(self): ...
    @hostname.setter
    def hostname(self, hostname: Any) -> None: ...
    @property
    def image_pull_secrets(self): ...
    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets: Any) -> None: ...
    @property
    def init_containers(self): ...
    @init_containers.setter
    def init_containers(self, init_containers: Any) -> None: ...
    @property
    def node_name(self): ...
    @node_name.setter
    def node_name(self, node_name: Any) -> None: ...
    @property
    def node_selector(self): ...
    @node_selector.setter
    def node_selector(self, node_selector: Any) -> None: ...
    @property
    def overhead(self): ...
    @overhead.setter
    def overhead(self, overhead: Any) -> None: ...
    @property
    def preemption_policy(self): ...
    @preemption_policy.setter
    def preemption_policy(self, preemption_policy: Any) -> None: ...
    @property
    def priority(self): ...
    @priority.setter
    def priority(self, priority: Any) -> None: ...
    @property
    def priority_class_name(self): ...
    @priority_class_name.setter
    def priority_class_name(self, priority_class_name: Any) -> None: ...
    @property
    def readiness_gates(self): ...
    @readiness_gates.setter
    def readiness_gates(self, readiness_gates: Any) -> None: ...
    @property
    def restart_policy(self): ...
    @restart_policy.setter
    def restart_policy(self, restart_policy: Any) -> None: ...
    @property
    def runtime_class_name(self): ...
    @runtime_class_name.setter
    def runtime_class_name(self, runtime_class_name: Any) -> None: ...
    @property
    def scheduler_name(self): ...
    @scheduler_name.setter
    def scheduler_name(self, scheduler_name: Any) -> None: ...
    @property
    def security_context(self): ...
    @security_context.setter
    def security_context(self, security_context: Any) -> None: ...
    @property
    def service_account(self): ...
    @service_account.setter
    def service_account(self, service_account: Any) -> None: ...
    @property
    def service_account_name(self): ...
    @service_account_name.setter
    def service_account_name(self, service_account_name: Any) -> None: ...
    @property
    def share_process_namespace(self): ...
    @share_process_namespace.setter
    def share_process_namespace(self, share_process_namespace: Any) -> None: ...
    @property
    def subdomain(self): ...
    @subdomain.setter
    def subdomain(self, subdomain: Any) -> None: ...
    @property
    def termination_grace_period_seconds(self): ...
    @termination_grace_period_seconds.setter
    def termination_grace_period_seconds(self, termination_grace_period_seconds: Any) -> None: ...
    @property
    def tolerations(self): ...
    @tolerations.setter
    def tolerations(self, tolerations: Any) -> None: ...
    @property
    def topology_spread_constraints(self): ...
    @topology_spread_constraints.setter
    def topology_spread_constraints(self, topology_spread_constraints: Any) -> None: ...
    @property
    def volumes(self): ...
    @volumes.setter
    def volumes(self, volumes: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
