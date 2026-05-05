from abc import ABC, abstractmethod

class FoodType:
    french = 1
    american = 2

class Restuarant(ABC):
    @abstractmethod
    def make_food(self):
        pass

    @abstractmethod
    def make_drink(self):
        pass

class FrenchRestuarant(Restuarant):
    def make_food(self):
        print('Beef Tehari')
    
    def make_drink(self):
        print('Merlot')

class AmericanRestuarant(Restuarant):
    def make_food(self):
        print('mamBurger')

    def make_drink(self):
        print('Coca Cola')

class RestuarantFactory:
    @staticmethod
    def suggest_restuarant(r_type: FoodType):
        if r_type == FoodType.french:
            return FrenchRestuarant()
        else:
            return AmericanRestuarant()

def dine_at(restuarant: Restuarant):
    restuarant.make_food()
    restuarant.make_drink()

if __name__ == '__main__':
    suggestion1 = RestuarantFactory.suggest_restuarant(FoodType.french)
    suggestion2 = RestuarantFactory.suggest_restuarant(FoodType.american)

    dine_at(suggestion1)
    dine_at(suggestion2)


