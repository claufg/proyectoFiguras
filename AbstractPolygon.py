from Form2D import Form2D

class AbstractPolygon(Form2D):
    def __init__(self, position=None, angle=0.0):
        super().__init__(position)
        if not (0.0 <= angle < 360.0):
            raise ValueError("Angle must be in [0.0, 360.0)")
        self.angle = angle

    def get_angle(self):
        return self.angle

    def rotate(self, degrees):
        if not (-360.0 < degrees < 360.0):
            raise ValueError("Rotation must be in (-360.0, 360.0)")
        self.angle = (self.angle + degrees) % 360.0

    def __eq__(self, other):
        return isinstance(other, AbstractPolygon) and super().__eq__(other) and self.angle == other.angle

    def __str__(self):
        return f"{super().__str__()},angle={self.angle}"

