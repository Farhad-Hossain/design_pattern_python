import random
from abc import ABC, abstractmethod

class Sprite:
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def move(self, x, y):
        pass

class FighterRank:
    private = 0
    sergeant = 1
    major = 2

class Fighter(Sprite):
    def __init__(self, rank):
        self.rank = rank
    
    def draw(self):
        print(f"Drawing fighter")

    def move(self):
        print(f"Moving fighter {self} to position {x}, {y}")

class FighterFactory:
    def __init__(self) -> None:
        self.fighters = []

    def get_fighter(self, rank: FighterRank):
        f = self.fighters[rank]
        self.fighters[rank] = f

        return f

class Army:
    army = []

    def spawn_fighter(self, rank: FighterRank):
        self.army.append(Fighter(rank))

    def draw_army(self):
        for fighter in self.army:
            if fighter.rank == FighterRank.major:
                print(f"M ", end="")
            elif fighter.rank == FighterRank.sergeant:
                print(f"S,", end="")
            else:
                print("P ", end="")

if __name__ == "__main__":
    army_size = 1000
    army = Army()

    for i in range(army_size):
        r = random.randrange(3)
        army.spawn_fighter(r)
    
    army.draw_army()
 
