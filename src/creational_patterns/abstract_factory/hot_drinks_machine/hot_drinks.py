from abc import ABCMeta


class HotDrink(metaclass=ABCMeta):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is nice but I\'d prefer it with milk')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')
