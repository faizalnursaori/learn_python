class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a circle with an area of {self.width * self.width}")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a circle with an area of {self.width * self.height / 2}")
        super().describe()

circle = Circle(color="Red", is_filled=True, radius=5)
square = Square(color="Blue", is_filled=False, width=5)
triangle = Triangle(color="Blue", is_filled=True, width=6, height=7)

print(circle.color)
print(circle.is_filled)
print(square.width)
print(triangle.width)
print(triangle.height)

square.describe()