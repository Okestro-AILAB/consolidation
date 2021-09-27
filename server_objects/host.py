# -*- coding: utf-8 -*-
import numpy as np


class Host:
    def __init__(self, vms=None, name=None, id=None, cluster_id=None, cluster_name=None, vcpu_total=None,
                 vcpu_used=None,
                 vcpu_free=None, vmemory_total=None, vmemory_used=None, vmemory_free=None):
        if vms is None:
            self.vms = dict()
        else:
            self.vms = vms

        self.id = id
        self.name = name

        self.cluster_id = cluster_id
        self.cluster_name = cluster_name

        self.vcpu_total = vcpu_total
        self.vcpu_used = vcpu_used
        self.vcpu_free = vcpu_free

        self.vmemory_total = vmemory_total
        self.vmemory_used = vmemory_used
        self.vmemory_free = vmemory_free

        self.sla_score = 0
        self.anomaly_score = 0
        self.workload_stability = 0

        self.cpu_workload = 0
        self.memory_workload = 0

        self.cpu_over_commit = 7
        self.memory_over_commit = 3

        self.is_idle = True

        self.idle_power = 0
        self.max_power = 0
        self.current_power = 0

    def add_vm(self, vm):
        self.vms[vm.name] = vm
        self.retrieve_vcpu_used()
        self.retrieve_vcpu_free()
        self.retrieve_memory_used()
        self.retrieve_memory_free()

    def pop_vm(self, vm):
        migrated_vm = self.vms.pop(vm.name, None)
        self.retrieve_vcpu_used()
        self.retrieve_vcpu_free()
        self.retrieve_memory_used()
        self.retrieve_memory_free()
        return migrated_vm

    def calculate_cpu_workload(self):
        for vm in self.vms.values():
            self.cpu_workload += vm.cpu_workload * vm.vcpu
        self.cpu_workload = self.cpu_workload / self.vcpu_total
        return self.cpu_workload

    def calculate_energy_consumption(self):
        if not self.is_idle:
            self.current_power = 0
        else:
            self.calculate_cpu_workload()
            self.current_power = self.idle_power + np.mean(self.cpu_workload) * (self.max_power - self.idle_power)
        return self.current_power

    def calculate_sla_score(self, threshold=50):
        self.calculate_cpu_workload()
        self.sla_score = sum(self.cpu_workload > threshold) / len(self.cpu_workload)
        return self.sla_score

    def calculate_anomaly_score(self, sigma=2):
        self.anomaly_score = sum(
            np.abs(self.cpu_workload - np.mean(self.cpu_workload)) > sigma * np.std(self.cpu_workload)) / len(
            self.cpu_workload)
        return self.anomaly_score

    def calculate_workload_stability(self):
        self.calculate_cpu_workload()
        self.workload_stability = 100 * (1 - self.calculate_anomaly_score()) * (1 - self.calculate_sla_score())
        return self.workload_stability

    def retrieve_vcpu_used(self):
        self.vcpu_used = 0
        for vm in self.vms.values():
            self.vcpu_used += vm.vcpu
        return self.vcpu_used

    def retrieve_vcpu_free(self):
        self.vcpu_free = self.vcpu_total * self.cpu_over_commit - self.retrieve_vcpu_used()
        return self.vcpu_free

    def retrieve_memory_used(self):
        self.vmemory_used = 0
        for vm in self.vms.values():
            self.vmemory_used += vm.vmemory
        return self.vmemory_used

    def retrieve_memory_free(self):
        self.vmemory_free = self.vmemory_total * self.memory_over_commit - self.retrieve_memory_used()
        return self.vmemory_free

    def sort_vms_by_vcpu(self, reverse=False):
        sorted_list = sorted(self.vms.items(), key=lambda vm: vm[1].vcpu, reverse=reverse)
        return sorted_list

    def __str__(self):
        return f"Host Object: {self.name}"

    def __repr__(self):
        return f"Host object: {self.name}"