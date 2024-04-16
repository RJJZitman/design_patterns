from order import Order
from cost_calculator import ShippingCostCalculator
from shipping_methods import StandardShipping, ExpressShipping


if __name__ == "__main__":
    # instantiate an order
    order = Order(weight=10, distance=100)

    # get calculators corresponding to different shipping methods
    standard_calculator = ShippingCostCalculator(StandardShipping())
    express_calculator = ShippingCostCalculator(ExpressShipping())

    # print shipping costs for the order per shipping method
    print("Standard Shipping Cost:", standard_calculator.calculate_shipping_cost(order))
    print("Express Shipping Cost:", express_calculator.calculate_shipping_cost(order))
