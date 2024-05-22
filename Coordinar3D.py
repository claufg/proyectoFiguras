import numpy as np

class Coordinate:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.position = np.array([x, y, z])

    def move(self, dx, dy, dz):
        self.position += np.array([dx, dy, dz])

    def get_position(self):
        return self.position

    def __eq__(self, other):
        return isinstance(other, Coordinate) and np.array_equal(self.position, other.position)

    def __str__(self):
        return f"Coordinate: {self.position}"
