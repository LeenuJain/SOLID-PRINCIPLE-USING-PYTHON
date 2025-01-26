from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_volume(self):
        pass

    @abstractmethod
    def calculate_peri(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_peri(self):
        return 2 * 3.14 * self.radius

    def calculate_volume(self):
        raise NotImplementedError("Circle does not have a volume!")

class Ractangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.breadth * self.length

    def calculate_volume(self):
        raise NotImplementedError("Ractangle does not have Volume!")

    def calculate_peri(self):
        return 2 * (self.length + self.breadth)

if __name__ == '__main__':
    circle = Circle(10)
    area = circle.calculate_area()
    perimeter = circle.calculate_peri()
    print(f"Area : {area} , Perimeter: {perimeter} ")

    ract = Ractangle(10, 20)
    ract.calculate_area()
    ract.calculate_volume() """raise NotImplementedError("Ractangle does not have Volume!")
NotImplementedError: Ractangle does not have Volume!"""