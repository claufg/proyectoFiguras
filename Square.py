from AbstractPolygon import AbstractPolygon

class Square(AbstractPolygon):
    def __init__(self, position=None, angle=0.0, side=0):
        super().__init__(position, angle)
        if side < 0:
            raise ValueError("El lado no puede ser negativo")
        self.side = side

    def get_side(self):
        return self.side

    def scale(self, percentage):
        if percentage <= 0:
            raise ValueError("El porcentaje de escalado debe ser positivo")
        self.side *= percentage / 100.0

    def clone(self):
        return Square(self.position.__copy__(), self.angle, self.side)

    def __str__(self):
        return f"{super().__str__()},side={self.side}"

    def __eq__(self, other):
        return isinstance(other, Square) and super().__eq__(other) and self.side == other.side
