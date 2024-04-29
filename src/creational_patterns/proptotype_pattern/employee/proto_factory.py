import copy

from employee import Employee, Address


class EmployeeFactory:
    """Factory to create employees with prototypes for different offices"""

    # Breaks OCP by hard-coding the prototypes and corresponding static methods
    main_office_employee = Employee(name="", address=Address(street_address="123 East Dr", suite=0, city="London"))
    aux_office_employee = Employee(name="", address=Address("123B East Dr", 0, "London"))

    @staticmethod
    def __new_employee(proto: Employee, name: str, suite: int) -> Employee:
        """Private method that should not be accessed by users. Returns a new Employee instance"""
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name: str, suite: int):
        return EmployeeFactory.__new_employee(proto=EmployeeFactory.main_office_employee, name=name, suite=suite)

    @staticmethod
    def new_aux_office_employee(name: str, suite: int):
        return EmployeeFactory.__new_employee(proto=EmployeeFactory.aux_office_employee, name=name, suite=suite)
