from Rectangle3D import Rectangle3D

class Square3D(Rectangle3D):
    def __init__(self, side_length, position=None, angles=None):
        super().__init__(side_length, side_length, position, angles)

    def get_side_length(self):
        return self.width

    def set_side_length(self, side_length):
        self.width = self.height = side_length

    def __eq__(self, other):
        return isinstance(other, Square3D) and super().__eq__(other)

    def __str__(self):
        return f"{super().__str__()}"
