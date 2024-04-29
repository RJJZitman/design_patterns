from vehicles import Car, Bike
from proto_factory import VehiclePrototypeFactory


if __name__ == "__main__":
    # registering prototype objects with the factory. Note that this approach allows for prototype definition per app
    # and does not break the OCP.
    VehiclePrototypeFactory.register_prototype("car", Car("Toyota", "Corolla"))
    VehiclePrototypeFactory.register_prototype("bike", Bike("Honda"))

    # dynamically creating instances based on user input
    while True:
        vehicle_type = input("Enter vehicle type (car/bike) or 'exit' to quit: ").lower()

        if vehicle_type == "exit":
            break

        # prototype = factory.create_prototype(vehicle_type)
        if prototype := VehiclePrototypeFactory.create_prototype(vehicle_type):
            print(f"Created new {vehicle_type.capitalize()}: {prototype}")
        else:
            print("Invalid vehicle type.")
