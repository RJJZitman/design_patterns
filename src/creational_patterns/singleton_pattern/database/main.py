from src.creational_patterns.singleton_pattern.singleton_deco import Singleton
from src.creational_patterns.singleton_pattern.singleton_metaclass import SingletonMeta


@Singleton
class DatabaseWithDeco:
    def __init__(self, x: int):
        self.x = x
        print('Init your database')


class DatabaseWithMeta(metaclass=SingletonMeta):
    def __init__(self, x: int):
        self.x = x
        print('Init your database')


if __name__ == '__main__':

    # test for database with decorator
    d1 = DatabaseWithDeco(x=1)
    d2 = DatabaseWithDeco(x=2)
    print(d1, d1.x)
    print(d2, d2.x)
    print(d1 == d2)

    print(75*"-")

    # test for database with metaclass
    d3 = DatabaseWithMeta(x=3)
    d4 = DatabaseWithMeta(x=4)
    print(d3, d3.x)
    print(d4, d4.x)
    print(d3 == d4)
