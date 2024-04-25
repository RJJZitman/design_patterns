from proto_factory import EmployeeFactory


if __name__ == "__main__":
    john = EmployeeFactory.new_aux_office_employee("John", 200)
    jane = EmployeeFactory.new_main_office_employee("Jane", 200)
    print(john)
    print(jane)
