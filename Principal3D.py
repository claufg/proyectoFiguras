from Circle import Circle
from Square import Square
from Rectangle import Rectangle
import matplotlib.pyplot as plt

# Crear instancias de las figuras
circle = Circle(center=(0, 0), radius=5)
square = Square(center=(0, 0), side=5)
rectangle = Rectangle(center=(0, 0), length=10, width=5)

# Plotear figuras en 3D
fig = plt.figure(figsize=(18, 6))

# Circle
ax1 = fig.add_subplot(131, projection='3d')
circle.plot_3d(ax1)

# Square
ax2 = fig.add_subplot(132, projection='3d')
square.plot_3d(ax2)

# Rectangle
ax3 = fig.add_subplot(133, projection='3d')
rectangle.plot_3d(ax3)

plt.show()

