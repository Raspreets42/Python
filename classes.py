from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Square):
    def __init__(self, radius):
        super().__init__(radius)

    # def area(self):
    #     return 3.14 * self.radius * self.radius

shapes = [Square(2), Triangle(4, 4), Circle(3)]
for shape in shapes:
    print(shape.area())