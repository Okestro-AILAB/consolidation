# -*- coding: utf-8 -*-
import copy
import uuid

class Consolidation:
    def __init__(self):
        self.uuid = uuid.uuid1()
        self.consolidation_id = ''
        self.workload_stability = 100
        self.energy_consumption = 0
        self.consolidation_model_type = ''
        self.number_server_shutdown = 0
        self.migrations = []
        self.cluster = None

    def add_migration(self, migration):
        self.migrations.append(migration)

    def save_cluster_status(self, cluster):
        self.cluster = copy.deepcopy(cluster)

    def calculate_energy_consumption(self):
        pass

    def calculate_workload_stability(self):
        pass

    def __str__(self):
        return f"number migrations: {len(self.migrations)}, number_server_shutdown: {self.number_server_shutdown} workload_stability: {self.workload_stability}"

    def __repr__(self):
        return f"number migrations: {len(self.migrations)}, number_server_shutdown: {self.number_server_shutdown} workload_stability: {self.workload_stability}"

