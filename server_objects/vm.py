# -*- coding: utf-8 -*-
class Vm:
    def __init__(self, id=None, name=None, is_idle=None, host_id=None, host_name=None, cluster_id=None, cluster_name=None, vcpu=None, vmemory=None, cpu_workload=0, memory_workload=0, is_duplicate=False, is_pinned=False):

        self.id = id
        self.name = name

        self.host_id = host_id
        self.host_name = host_name

        self.cluster_id = cluster_id
        self.cluster_name = cluster_name

        self.vcpu = vcpu
        self.vmemory = vmemory

        self.cpu_workload = cpu_workload
        self.memory_workload = memory_workload

        self.is_idle = is_idle # on off 정보를 저장하기 위함
        self.is_duplicate = is_duplicate # 복사된 vm인지
        self.is_pinned = is_pinned # 움직이면 안되는 vm

    def __str__(self):
        return f"Vm Object: {self.name}"

    def __repr__(self):
        return f"Vm object: {self.name}"
