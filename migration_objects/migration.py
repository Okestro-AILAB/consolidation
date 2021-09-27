# -*- coding: utf-8 -*-
class Migration():
    def __init__(self, to_host_id=None, to_host_name=None, vm_id=None, vm_name=None, from_host_id=None, from_host_name=None,
                 description=None, vm=None):
        self.to_host_id = to_host_id
        self.to_host_name = to_host_name
        self.vm_id = vm_id
        self.vm_name = vm_name
        self.from_host_id = from_host_id
        self.from_host_name = from_host_name
        self.description = description
        self.vm = vm

    def __str__(self):
        return f"Migration Object: vm:{self.vm_name} from:{self.from_host_name} to:{self.to_host_name}"

    def __repr__(self):
        return f"Migration Object: vm:{self.vm_name} from:{self.from_host_name} to:{self.to_host_name}"
