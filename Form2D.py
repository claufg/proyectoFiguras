from Coordinate import Coordinate
from abc import ABC, abstractmethod

class Form2D(ABC):
    def __init__(self, position = None):
        self.position = position if position else Coordinate()

    def get_position(self):
        return self.position

    def move(self, new_position):
        old_position = self.position
        self.position = new_position if new_position else self.position
        return old_position

    def __str__(self):
        return str(self.position)

    def __eq__(self, other):
        return isinstance(other, Form2D) and self.position == other.position

    def clone_with_new_position(self, new_position):
        cloned = self.clone()
        cloned.move(new_position)
        return cloned
    
    @abstractmethod
    def clone(self):
        pass
    
    @abstractmethod
    def scale(self, percentage):
        pass
