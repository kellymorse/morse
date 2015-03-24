import logging; logger = logging.getLogger("morse." + __name__)
from morse.middleware import AbstractDatastream

class AbstractHLAOutput(AbstractDatastream):
    def initialize(self):
        self.amb = self.kwargs['__hla_node'].morse_ambassador
        self._obj = None

    def register_object(self, handle):
        self._obj = self.amb.register_object(handle, \
                    self.component_instance.robot_parent.name())

    def update_attribute(self, to_send):
        self.amb.update_attribute(self._obj, to_send)

class AbstractHLAInput(AbstractDatastream):
    def initialize(self):
        self.amb = self.kwargs['__hla_node'].morse_ambassador
        self._amb = self.kwargs['__hla_node'].morse_ambassador
        self._hla_name = self.component_instance.robot_parent.name() 

    def suscribe_attributes(self, obj_handle, attr_handles):
        self.amb.suscribe_attributes(self._hla_name, obj_handle, attr_handles)

    def get_attributes(self):
        return self.amb.get_attributes(self._hla_name)

    def hla_name(self):
        return self._hla_name