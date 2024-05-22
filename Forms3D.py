import numpy as np
from abc import ABC

class Form3D(ABC):
    def __init__(self, position=None):
        if position is None:
            position = np.array([0.0, 0.0, 0.0])
        elif len(position) != 3:
            raise ValueError("Position must be a 3D coordinate")
        self.position = np.array(position)

    def move(self, displacement):
        if len(displacement) != 3:
            raise ValueError("Displacement must be a 3D vector")
        self.position += np.array(displacement)

    def get_position(self):
        return self.position

    def __eq__(self, other):
        return isinstance(other, Form3D) and np.array_equal(self.position, other.position)

    def __str__(self):
        return f"position={self.position}"
