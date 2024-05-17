from e_commerce_facade import EcommerceFacade


def main():
    facade = EcommerceFacade()

    customer_id = 101
    items = ["item1", "item2", "item3"]
    payment_details = {"card_number": "1234-5678-9012-3456", "expiry_date": "12/25", "cvv": "123"}
    shipping_address = "123 Main St, Anytown, USA"

    # Place an order
    if facade.place_order(customer_id, items, payment_details, shipping_address):
        print("Order processing completed successfully.")

    # Track an order
    order_id = 123  # Assuming this is the order ID from the placed order
    facade.track_order(order_id)

    # Cancel an order
    facade.cancel_order(order_id)

    # Low-level operations
    facade.restock_inventory(["item1", "item2"])
    facade.check_inventory(["item1", "item2"])
    facade.process_payment(order_id, payment_details)


if __name__ == "__main__":
    main()
