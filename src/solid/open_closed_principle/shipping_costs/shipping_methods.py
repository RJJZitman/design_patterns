from abc import ABCMeta, abstractmethod

from order import Order


class ShippingStrategy(metaclass=ABCMeta):
    """Interface for shipping strategies"""
    @abstractmethod
    def calculate_cost(self, order):
        pass


class StandardShipping(ShippingStrategy):
    """Implementation of ShippingStrategy for standard shipping"""
    def calculate_cost(self, order: Order):
        """Calculates the cost for an order for standard shipment"""
        # Standard shipping cost calculation logic
        return order.weight * 0.5 + order.distance * 0.1


class ExpressShipping(ShippingStrategy):
    """Implementation of ShippingStrategy for express shipping"""
    def calculate_cost(self, order: Order):
        """Calculates the cost for an order for express shipment"""
        # Express shipping cost calculation logic
        return order.weight * 0.8 + order.distance * 0.3
