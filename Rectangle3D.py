from AbstractPolygon import AbstractPolygon

class Rectangle3D(AbstractPolygon):
    def __init__(self, width, height, position=None, angles=None):
        super().__init__(position, angles)
        self.width = width
        self.height = height

    def get_dimensions(self):
        return self.width, self.height

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return isinstance(other, Rectangle3D) and super().__eq__(other) and self.width == other.width and self.height == other.height

    def __str__(self):
        return f"{super().__str__()}, width={self.width}, height={self.height}"
