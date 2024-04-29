from abc import ABCMeta

from hot_drinks import Tea, Coffee


class HotDrinkFactory(metaclass=ABCMeta):
    """Interface for HotDrink factories"""
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    """Tea factory"""
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    """Coffee factory"""
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()
