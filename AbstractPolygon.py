from Form3D import Form3D

class AbstractPolygon(Form3D):
    def __init__(self, position=None, angles=None):
        super().__init__(position)
        if angles is None:
            angles = [0.0, 0.0, 0.0]
        if not all(0.0 <= angle < 360.0 for angle in angles):
            raise ValueError("Angles must be in [0.0, 360.0)")
        self.angles = np.array(angles)

    def get_angles(self):
        return self.angles

    def rotate(self, degrees):
        if len(degrees) != 3:
            raise ValueError("Rotation must be a 3D vector")
        if not all(-360.0 < degree < 360.0 for degree in degrees):
            raise ValueError("Rotation degrees must be in (-360.0, 360.0)")
        self.angles = (self.angles + np.array(degrees)) % 360.0

    def __eq__(self, other):
        return isinstance(other, AbstractPolygon) and super().__eq__(other) and np.array_equal(self.angles, other.angles)

    def __str__(self):
        return f"{super().__str__()},angles={self.angles}"
