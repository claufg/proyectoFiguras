import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Rectangle(Form2D):
    # Código existente...

    def plot_3d(self, ax=None):
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
        points = np.array([[0, 0, 0], [0, self.width, 0], [self.length, self.width, 0], [self.length, 0, 0]])
        verts = [list(zip(points[:, 0], points[:, 1], points[:, 2]))]
        ax.add_collection3d(Poly3DCollection(verts, alpha=.25, linewidths=1, edgecolors='r'))
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Representation of Rectangle')
        ax.set_xlim([0, self.length])
        ax.set_ylim([0, self.width])
        ax.set_zlim([0, max(self.length, self.width)])

