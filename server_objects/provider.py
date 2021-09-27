# -*- coding: utf-8 -*-
from .cluster import Cluster


class Provider:

    def __init__(self, clusters=None, hosts=None, vms=None, cpu_threshold=70, memory_threshold=70, id=None, name=None):

        if clusters is None:
            self.clusters = dict()
        else:
            self.clusters = None
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
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold
        self.hosts = dict()
        self.vms = dict()

    def __str__(self):
        return f"Provider Object: {self.name}"

    def __repr__(self):
        return f"Provider object: {self.name}"