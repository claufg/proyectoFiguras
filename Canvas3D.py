import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Canvas:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for shape in self.shapes:
            position = shape.get_position()
            if isinstance(shape, Circle3D):
                ax.scatter(*position, marker='o', label='Circle')
            elif isinstance(shape, Rectangle3D):
                ax.scatter(*position, marker='s', label='Rectangle')
            elif isinstance(shape, Square3D):
                ax.scatter(*position, marker='^', label='Square')

        plt.legend()
        plt.show()
