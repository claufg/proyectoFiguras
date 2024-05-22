from Form2D import Form2D

class Circle(Form2D):
    def __init__(self, position=None, radius=0):
        super().__init__(position)
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def get_radius(self):
        return self.radius

    def scale(self, percentage):
        if percentage <= 0:
            raise ValueError("Scale percentage must be positive")
        self.radius *= percentage / 100.0

    def clone(self):
        return Circle(self.position.__copy__(), self.radius)

    def __str__(self):
        return f"{super().__str__()},radius={self.radius}"

    def __eq__(self, other):
        return isinstance(other, Circle) and super().__eq__(other) and self.radius == other.radius
