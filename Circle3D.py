from Form3D import Form3D

class Circle3D(Form3D):
    def __init__(self, radius, position=None):
        super().__init__(position)
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return isinstance(other, Circle3D) and super().__eq__(other) and self.radius == other.radius

    def __str__(self):
        return f"{super().__str__()}, radius={self.radius}"
