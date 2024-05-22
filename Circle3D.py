import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Circle(Form2D):
    # Código existente...

    def plot_3d(self, ax=None):
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
        u = np.linspace(0, 2 * np.pi, 100)
        x = self.radius * np.cos(u)
        y = self.radius * np.sin(u)
        z = np.zeros_like(u)
        ax.plot(x, y, z)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Representation of Circle')

