# -*- coding: utf-8 -*-
import uuid


class TotalConsolidation:

    def __init__(self):
        self.consolidations = dict()
        self.uuid = uuid.uuid4()

    def add_consolidation(self, consolidation_name, consolidation):
        self.consolidations[consolidation_name] = consolidation

    def __str__(self):
        return f"number consolidations: {len(self.consolidations)}"

    def __repr__(self):
        return f"number consolidations: {len(self.consolidations)}"
