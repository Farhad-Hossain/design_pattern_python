import copy
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Square(Shape):
    def __init__(self, size):
        self.size = size

    def draw(self):
        print(f"Drawinf a Square of size {self.size}")

class Circle(Shape):
    def __init__(self, radius: int = 0):
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")
    
class AbstractArt(Shape):
    def __init__(self, bg_color, shapes):
        self.bg_color = bg_color
        self.shapes = shapes
    
    def draw(self):
        print(f"Drawing an Abstract SHape .... ")
        [x.draw() for x in self.shapes]

if __name__ == '__main__':
    shapes = [Square(4), Square(9), Circle('lklkj')]

    art1 = AbstractArt('red', shapes)
    art2 = copy.copy(art1)

    art1.draw()
    art2.draw()


