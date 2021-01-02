# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1PersistentVolumeSpec:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, access_modes: Optional[Any] = ..., aws_elastic_block_store: Optional[Any] = ..., azure_disk: Optional[Any] = ..., azure_file: Optional[Any] = ..., capacity: Optional[Any] = ..., cephfs: Optional[Any] = ..., cinder: Optional[Any] = ..., claim_ref: Optional[Any] = ..., csi: Optional[Any] = ..., fc: Optional[Any] = ..., flex_volume: Optional[Any] = ..., flocker: Optional[Any] = ..., gce_persistent_disk: Optional[Any] = ..., glusterfs: Optional[Any] = ..., host_path: Optional[Any] = ..., iscsi: Optional[Any] = ..., local: Optional[Any] = ..., mount_options: Optional[Any] = ..., nfs: Optional[Any] = ..., node_affinity: Optional[Any] = ..., persistent_volume_reclaim_policy: Optional[Any] = ..., photon_persistent_disk: Optional[Any] = ..., portworx_volume: Optional[Any] = ..., quobyte: Optional[Any] = ..., rbd: Optional[Any] = ..., scale_io: Optional[Any] = ..., storage_class_name: Optional[Any] = ..., storageos: Optional[Any] = ..., volume_mode: Optional[Any] = ..., vsphere_volume: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def access_modes(self): ...
    @access_modes.setter
    def access_modes(self, access_modes: Any) -> None: ...
    @property
    def aws_elastic_block_store(self): ...
    @aws_elastic_block_store.setter
    def aws_elastic_block_store(self, aws_elastic_block_store: Any) -> None: ...
    @property
    def azure_disk(self): ...
    @azure_disk.setter
    def azure_disk(self, azure_disk: Any) -> None: ...
    @property
    def azure_file(self): ...
    @azure_file.setter
    def azure_file(self, azure_file: Any) -> None: ...
    @property
    def capacity(self): ...
    @capacity.setter
    def capacity(self, capacity: Any) -> None: ...
    @property
    def cephfs(self): ...
    @cephfs.setter
    def cephfs(self, cephfs: Any) -> None: ...
    @property
    def cinder(self): ...
    @cinder.setter
    def cinder(self, cinder: Any) -> None: ...
    @property
    def claim_ref(self): ...
    @claim_ref.setter
    def claim_ref(self, claim_ref: Any) -> None: ...
    @property
    def csi(self): ...
    @csi.setter
    def csi(self, csi: Any) -> None: ...
    @property
    def fc(self): ...
    @fc.setter
    def fc(self, fc: Any) -> None: ...
    @property
    def flex_volume(self): ...
    @flex_volume.setter
    def flex_volume(self, flex_volume: Any) -> None: ...
    @property
    def flocker(self): ...
    @flocker.setter
    def flocker(self, flocker: Any) -> None: ...
    @property
    def gce_persistent_disk(self): ...
    @gce_persistent_disk.setter
    def gce_persistent_disk(self, gce_persistent_disk: Any) -> None: ...
    @property
    def glusterfs(self): ...
    @glusterfs.setter
    def glusterfs(self, glusterfs: Any) -> None: ...
    @property
    def host_path(self): ...
    @host_path.setter
    def host_path(self, host_path: Any) -> None: ...
    @property
    def iscsi(self): ...
    @iscsi.setter
    def iscsi(self, iscsi: Any) -> None: ...
    @property
    def local(self): ...
    @local.setter
    def local(self, local: Any) -> None: ...
    @property
    def mount_options(self): ...
    @mount_options.setter
    def mount_options(self, mount_options: Any) -> None: ...
    @property
    def nfs(self): ...
    @nfs.setter
    def nfs(self, nfs: Any) -> None: ...
    @property
    def node_affinity(self): ...
    @node_affinity.setter
    def node_affinity(self, node_affinity: Any) -> None: ...
    @property
    def persistent_volume_reclaim_policy(self): ...
    @persistent_volume_reclaim_policy.setter
    def persistent_volume_reclaim_policy(self, persistent_volume_reclaim_policy: Any) -> None: ...
    @property
    def photon_persistent_disk(self): ...
    @photon_persistent_disk.setter
    def photon_persistent_disk(self, photon_persistent_disk: Any) -> None: ...
    @property
    def portworx_volume(self): ...
    @portworx_volume.setter
    def portworx_volume(self, portworx_volume: Any) -> None: ...
    @property
    def quobyte(self): ...
    @quobyte.setter
    def quobyte(self, quobyte: Any) -> None: ...
    @property
    def rbd(self): ...
    @rbd.setter
    def rbd(self, rbd: Any) -> None: ...
    @property
    def scale_io(self): ...
    @scale_io.setter
    def scale_io(self, scale_io: Any) -> None: ...
    @property
    def storage_class_name(self): ...
    @storage_class_name.setter
    def storage_class_name(self, storage_class_name: Any) -> None: ...
    @property
    def storageos(self): ...
    @storageos.setter
    def storageos(self, storageos: Any) -> None: ...
    @property
    def volume_mode(self): ...
    @volume_mode.setter
    def volume_mode(self, volume_mode: Any) -> None: ...
    @property
    def vsphere_volume(self): ...
    @vsphere_volume.setter
    def vsphere_volume(self, vsphere_volume: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
