import copy

from vehicles import IVehiclePrototype


class VehiclePrototypeFactory:
    """A vehicle prototype factory that allows for dynamic prototype definition and construction"""
    prototypes = {}

    @staticmethod
    def _new_vehicle_proto_instance(proto: IVehiclePrototype) -> IVehiclePrototype:
        return copy.deepcopy(proto)

    @staticmethod
    def register_prototype(key: str, proto: IVehiclePrototype):
        VehiclePrototypeFactory.prototypes[key] = proto

    @staticmethod
    def create_prototype(key: str) -> IVehiclePrototype | None:
        if proto := VehiclePrototypeFactory.prototypes.get(key):
            return VehiclePrototypeFactory._new_vehicle_proto_instance(proto=proto)
        else:
            return None
