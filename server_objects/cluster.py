# -*- coding: utf-8 -*-
import numpy as np

from .host import Host

class Cluster:
    def __init__(self, id='', provider_type='', hosts=None, vms=None, name=None, cpu_type=None):
        if hosts is None:
            self.hosts = dict()
        else:
            self.hosts = vms
        if vms is None:
            self.vms = dict()
        else:
            self.vms = vms

        self.id = id
        self.name = name

        self.provider_type = provider_type
        self.cpu_type = cpu_type

        self.sd = 0
        self.workload_stability = 100
        self.energy_consumption = 0

    def set_over_commit(self, cpu_over_commit, memory_over_commit):
        for host in self.hosts:
            host.cpu_over_commit = cpu_over_commit
            host.memory_over_commitb = memory_over_commit

    def calculate_workload_stability(self):
        try:
            self.workload_stability = 0
            count = 0
            for host in self.hosts.values():
                if host.vms:
                    self.workload_stability += host.calculate_workload_stability()
                    count += 1
            self.workload_stability = self.workload_stability / count
            return self.workload_stability

        except:
            self.workload_stability = 100
            return self.workload_stability

    def calculate_energy_consumption(self):
        self.energy_consumption = 0
        for hostname, host in self.hosts.items():
            self.energy_consumption += host.calculate_energy_consumption()
        return self.energy_consumption

    def calculate_sd(self):
        list_for_std = [host.vcpu_used for host in self.hosts.values()]
        self.sd = np.std(list_for_std)
        return self.sd

    def sort_hosts_by_vcpu_total(self, reverse=False):
        sorted_list = sorted(self.hosts.items(), key=lambda host: host[1].vcpu_total, reverse=reverse)
        return sorted_list

    def sort_hosts_by_vcpu_used(self, reverse=False):
        sorted_list = sorted(self.hosts.items(), key=lambda host: host[1].retrieve_vcpu_used(), reverse=reverse)
        return sorted_list

    def sort_hosts_by_memory_total(self, reverse=False):
        sorted_list = sorted(self.hosts.items(), key=lambda host: host[1].vmemory_total, reverse=reverse)
        return sorted_list

    def sort_hosts_by_memory_used(self, reverse=False):
        sorted_list = sorted(self.hosts.items(), key=lambda host: host[1].retrieve_memory_used(), reverse=reverse)
        return sorted_list

    def __str__(self):
        return f"Cluster Object: {self.name}"

    def __repr__(self):
        return f"Cluster object: {self.name}"