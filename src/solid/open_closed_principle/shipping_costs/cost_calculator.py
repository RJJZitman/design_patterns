from order import Order
from shipping_methods import ShippingStrategy


class ShippingCostCalculator:
    """
    Calculator class which takes a certain shipping strategy to make the required calculations.
    """
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def calculate_shipping_cost(self, order: Order) -> float:
        """Calculates the actual shipping costs for an order"""
        return self.strategy.calculate_cost(order)
