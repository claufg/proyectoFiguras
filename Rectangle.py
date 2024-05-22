from AbstractPolygon import AbstractPolygon

class Rectangle(AbstractPolygon):
    def __init__(self, position=None, angle=0.0, length=0, width=0):
        super().__init__(position, angle)
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative")
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def scale(self, percentage):
        if percentage <= 0:
            raise ValueError("Scale percentage must be positive")
        self.length *= percentage / 100.0
        self.width *= percentage / 100.0

    def clone(self):
        return Rectangle(self.position.__copy__(), self.angle, self.length, self.width)

    def __str__(self):
        return f"{super().__str__()},length={self.length},width={self.width}"

    def __eq__(self, other):
        return isinstance(other, Rectangle) and super().__eq__(other) and self.length == other.length and self.width == other.width
