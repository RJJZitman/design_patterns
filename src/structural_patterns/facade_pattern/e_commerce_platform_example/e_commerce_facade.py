from platform_parts import OrderProcessor, PaymentGateway, InventoryManager, ShippingService


class EcommerceFacade:
    """
    Provides a facade for the platform parts and provides them as a single whole to manage orders, payments,
    inventory and shipping services
    """
    def __init__(self):
        """Initialise all low level platform parts"""
        self.order_processor = OrderProcessor()
        self.payment_gateway = PaymentGateway()
        self.inventory_manager = InventoryManager()
        self.shipping_service = ShippingService()

    def place_order(self, customer_id: int, items: list, payment_details: dict, shipping_address: str):
        """
        Places an order if the items are in stock. Order placement includes payment processing, inventory updates
        and providing shipping
        """
        # Step 1: Check inventory
        if not self.inventory_manager.check_inventory(items):
            print("Some items are out of stock")
            return False

        # Step 2: Create order
        order_id = self.order_processor.create_order(customer_id, items)

        # Step 3: Process payment
        if not self.payment_gateway.process_payment(order_id, payment_details):
            print("Payment processing failed")
            return False

        # Step 4: Update inventory
        self.inventory_manager.update_inventory(items)

        # Step 5: Arrange shipping
        self.shipping_service.arrange_shipping(order_id, shipping_address)

        print("Order placed successfully")
        return True

    def cancel_order(self, order_id: int):
        """Cancel order via the OrderProcessor"""
        self.order_processor.cancel_order(order_id)
        self.payment_gateway.refund_payment(order_id)
        print(f"Order {order_id} has been cancelled and refunded")

    def track_order(self, order_id: int):
        """Track order via the ShippingService"""
        status = self.shipping_service.track_order(order_id)
        print(f"Order {order_id} status: {status}")
        return status

    # Exposing low-level operations for advanced users
    def check_inventory(self, items: list):
        """Check inventory via the InventoryManager"""
        return self.inventory_manager.check_inventory(items)

    def restock_inventory(self, items: list):
        """Restock inventory via the InventoryManager"""
        self.inventory_manager.restock_inventory(items)

    def process_payment(self, order_id: int, payment_details: dict):
        """Process a payment via the PaymentGateway"""
        return self.payment_gateway.process_payment(order_id, payment_details)
