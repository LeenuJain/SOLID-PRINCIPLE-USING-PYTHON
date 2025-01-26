from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def display_result(self):
        pass

# Interface for 2D Shapes
class Shape2D(Shape):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

# Interface for 3D Shapes
class Shape3D(Shape):
    @abstractmethod
    def calculate_volume(self):
        pass

    @abstractmethod
    def calculate_surface_area(self):
        pass

class Circle(Shape2D):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    def display_result(self):
        print(f"Circle Area : {self.calculate_area()}, Circle Perimeter : {self.calculate_perimeter()}")


class Cube(Shape3D):
    def __init__(self, side):
        self.side = side

    def calculate_volume(self):
        return self.side ** 3

    def calculate_surface_area(self):
        return 6 * (self.side ** 2)

    def display_result(self):
        print(f"Cube Volume : {self.calculate_volume()} , Cube Surface Area : {self.calculate_surface_area()}")


if __name__ == "__main__":
    circle_obj = Circle(10)
    circle_obj.display_result()

    cube_obj = Cube(20)
    cube_obj.display_result()

"""
Circle Area : 314.0, Circle Perimeter : 62.800000000000004
Cube Volume : 8000 , Cube Surface Area : 2400
"""
