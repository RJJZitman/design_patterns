from person import Person


# note that this implementation of a builder with sub-builders breaks the ocp
class PersonBuilder:
    """Builder for Person objects by utilising sub-builders"""
    def __init__(self, person: Person | None = None):
        if person is None:
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        """Returns the Person object"""
        return self.person


class PersonJobBuilder(PersonBuilder):
    """Sub-builder for living information of a Person"""
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name: str):
        self.person.company_name = company_name
        return self

    def as_a(self, position: str):
        self.person.position = position
        return self

    def earning(self, annual_income: str | int):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address: str):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode: str):
        self.person.postcode = postcode
        return self

    def in_city(self, city: str):
        self.person.city = city
        return self

