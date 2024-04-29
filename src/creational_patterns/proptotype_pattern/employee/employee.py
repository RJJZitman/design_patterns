class Address:
    """Address class to hold address data"""
    def __init__(self, street_address: str, suite: int, city: str):
        self.suite = suite
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'


class Employee:
    """Employee class to hold employee data"""
    def __init__(self, name: str, address: Address):
        self.address = address
        self.name = name

    def __str__(self):
        return f'{self.name} works at {self.address}'
