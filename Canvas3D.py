import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Canvas:
    # Código existente...

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for shape in self.shapes:
            shape.plot_3d(ax)
        plt.show()
