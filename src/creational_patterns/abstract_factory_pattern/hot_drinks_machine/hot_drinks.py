from abc import ABCMeta


class HotDrink(metaclass=ABCMeta):
    """Interface for hot drinks"""
    def consume(self):
        pass


class Tea(HotDrink):
    """Implementation for tea"""
    def consume(self):
        print('This tea is nice but I\'d prefer it with milk')


class Coffee(HotDrink):
    """Implementation for coffee"""
    def consume(self):
        print('This coffee is delicious')
