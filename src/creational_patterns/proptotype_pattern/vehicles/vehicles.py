from abc import ABCMeta, abstractmethod


class IVehiclePrototype(metaclass=ABCMeta):

    @abstractmethod
    def use_break(self, force: float):
        ...


class Car(IVehiclePrototype):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"Car: {self.make} {self.model}"

    def use_break(self, force: float):
        ...


class Bike(IVehiclePrototype):
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Bike: {self.brand}"

    def use_break(self, force: float):
        ...
