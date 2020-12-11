import abc

class Shape:

    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height * self.width)

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width ** 2

    def calculate_perimeter(self):
        return 4* self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

class ShapeFacory:
    @classmethod
    def create_shape(cls, name):
        if name == 'circle':
            radius = input("Enter the radius of Circle: ")
            return Circle(float(radius))

        if name == "rectangle":
            height = input("Enter the Height of the Rectange: ")
            width = input("Enter the Width of the Rectangle: ")
            return Rectangle(int(height), int(width))

        if name == "square":
            width = input('Enter the width of the Square: ')
            return Square(int(width))

def shapes_client():
    # shapeFactory = ShapeFacory()
    shape_name = input("Enter the name of the shape: ")
    
    shape = ShapeFacory.create_shape(shape_name)
    print(f'The type of object created : {type(shape)}')
    print(f'The Area of the {shape_name} is: {shape.calculate_area()}')
    print(f'The Perimeter of the {shape_name} is: {shape.calculate_perimeter()}')

if __name__ == "__main__":
    shapes_client()         # rectangle (or)  square   (or)    circle