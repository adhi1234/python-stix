# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# mixbox
from mixbox import fields

# stix
import stix
import stix.bindings.ttp as ttp_binding

from .malware_instance import MalwareInstance
from .exploit import Exploit
from .attack_pattern import AttackPattern

from mixbox import entities, fields

class Behavior(entities.Entity):
    _binding = ttp_binding
    _binding_class = _binding.BehaviorType
    _namespace = "http://stix.mitre.org/TTP-1"

    malware_instances = fields.TypedField("Malware", type_="stix.ttp.behavior.MalwareInstances", key_name="malware_instances")
    attack_patterns = fields.TypedField("Attack_Patterns", type_="stix.ttp.behavior.AttackPatterns")
    exploits = fields.TypedField("Exploits", type_="stix.ttp.behavior.Exploits")

    def __init__(self, malware_instances=None, attack_patterns=None, exploits=None):
        super(Behavior, self).__init__()
        self.malware_instances = malware_instances
        self.attack_patterns = attack_patterns
        self.exploits = exploits


    def add_malware_instance(self, malware):
        self.malware_instances.append(malware)

    def add_attack_pattern(self, attack_pattern):
        self.attack_patterns.append(attack_pattern)

    def add_exploit(self, exploit):
        self.exploits.append(exploit)

#     def to_obj(self, return_obj=None, ns_info=None):
#         super(Behavior, self).to_obj(return_obj=return_obj, ns_info=ns_info)
# 
#         if not return_obj:
#             return_obj = self._binding_class()
# 
#         if self.malware_instances:
#             return_obj.Malware = self.malware_instances.to_obj(ns_info=ns_info)
#         if self.exploits:
#             return_obj.Exploits = self.exploits.to_obj(ns_info=ns_info)
#         if self.attack_patterns:
#             return_obj.Attack_Patterns = self.attack_patterns.to_obj(ns_info=ns_info)
# 
#         return return_obj
# 
#     @classmethod
#     def from_obj(cls, obj, return_obj=None):
#         if not obj:
#             return None
# 
#         if not return_obj:
#             return_obj = cls()
# 
#         return_obj.malware_instances = MalwareInstances.from_obj(obj.Malware)
#         return_obj.exploits = Exploits.from_obj(obj.Exploits)
#         return_obj.attack_patterns = AttackPatterns.from_obj(obj.Attack_Patterns)
# 
#         return return_obj
# 
#     def to_dict(self):
#         return super(Behavior, self).to_dict()
# 
#     @classmethod
#     def from_dict(cls, dict_repr, return_obj=None):
#         if not dict_repr:
#             return None
#         if not return_obj:
#             return_obj = cls()
# 
#         get = dict_repr.get
# 
#         return_obj.malware_instances = MalwareInstances.from_dict(get('malware_instances'))
#         return_obj.exploits = Exploits.from_dict(get('exploits'))
#         return_obj.attack_patterns = AttackPatterns.from_dict(get('attack_patterns'))
# 
#         return return_obj


class Exploits(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _contained_type = Exploit
    _binding = ttp_binding
    _binding_class = _binding.ExploitsType

    exploit = fields.TypedField("Exploit", Exploit, multiple=True, key_name="exploits")


class MalwareInstances(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _binding = ttp_binding
    _binding_class = _binding.MalwareType

    malware_instance = fields.TypedField("Malware_Instance", MalwareInstance, multiple=True, key_name="malware_instances")


class AttackPatterns(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _binding = ttp_binding
    _binding_class = _binding.AttackPatternsType

    attack_pattern = fields.TypedField("Attack_Pattern", AttackPattern, multiple=True, key_name="attack_patterns")
