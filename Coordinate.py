class Coordinate:
    NOT_VALID = float('nan')
    MAX_VALUE = 32767.9999
    MIN_VALUE = -32767.9999

    def __init__(self, x=NOT_VALID, y=NOT_VALID):
        if x < self.MIN_VALUE or x > self.MAX_VALUE or y < self.MIN_VALUE or y > self.MAX_VALUE:
            raise ValueError("Coordinates out of range")
        self.x = x
        self.y = y

    def __copy__(self):
        return Coordinate(self.x, self.y)

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return isinstance(other, Coordinate) and self.x == other.x and self.y == other.y

    def sum(self, other):
        result_x = self.x + other.x
        result_y = self.y + other.y
        if result_x < self.MIN_VALUE or result_x > self.MAX_VALUE or result_y < self.MIN_VALUE or result_y > self.MAX_VALUE:
            raise ArithmeticError("Resulting coordinate out of range")
        return Coordinate(result_x, result_y)

    def subtract(self, other):
        result_x = self.x - other.x
        result_y = self.y - other.y
        if result_x < self.MIN_VALUE or result_x > self.MAX_VALUE or result_y < self.MIN_VALUE or result_y > self.MAX_VALUE:
            raise ArithmeticError("Resulting coordinate out of range")
        return Coordinate(result_x, result_y)

