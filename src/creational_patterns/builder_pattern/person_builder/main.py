from builders import PersonBuilder


if __name__ == '__main__':
    pb = PersonBuilder()
    p = (pb
         .lives
            .at('streetname, number')
            .in_city('place')
            .with_postcode('1234AB')
         .works
            .at('Organisation')
            .as_a('employee')
            .earning(100000)
         .build())
    print(p)
    person2 = PersonBuilder().build()
    print(person2)
