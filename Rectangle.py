from AbstractPolygon import AbstractPolygon

class Rectangle(AbstractPolygon):
    """
    Clase para representar un rectángulo, heredando de AbstractPolygon.

    Attributes
    ----------
    position : Coordinate
        Coordenada de la esquina superior izquierda del rectángulo.
    angle : float
        Ángulo de rotación del rectángulo en grados.
    length : float
        Longitud del rectángulo.
    width : float
        Ancho del rectángulo.

    Methods
    -------
    get_length():
        Devuelve la longitud del rectángulo.
    get_width():
        Devuelve el ancho del rectángulo.
    scale(percentage):
        Escala el rectángulo en un porcentaje dado.
    clone():
        Crea y devuelve una copia de este rectángulo.
    __str__():
        Devuelve una representación en cadena del rectángulo.
    __eq__(other):
        Comprueba la igualdad con otro rectángulo.
    """

    def __init__(self, position=None, angle=0.0, length=0, width=0):
        """
        Inicializa una nueva instancia de Rectangle.

        Parameters
        ----------
        position : Coordinate, optional
            La posición de la esquina superior izquierda del rectángulo (default is None).
        angle : float, optional
            El ángulo de rotación del rectángulo en grados (default is 0.0).
        length : float, optional
            La longitud del rectángulo (default is 0).
        width : float, optional
            El ancho del rectángulo (default is 0).

        Raises
        ------
        ValueError
            Si la longitud o el ancho son negativos.
        """
        # Inicialización del rectángulo llamando al constructor de la clase base.
        super().__init__(position, angle)
        # Validación de que la longitud y el ancho no sean negativos.
        if length < 0 or width < 0:
            raise ValueError("El ancho y el alto no pueden ser negativos")
        self.length = length
        self.width = width

    def get_length(self):
        """
        Devuelve la longitud del rectángulo.

        Returns
        -------
        float
            La longitud del rectángulo.
        """
        return self.length

    def get_width(self):
        """
        Devuelve el ancho del rectángulo.

        Returns
        -------
        float
            El ancho del rectángulo.
        """
        return self.width

    def scale(self, percentage):
        """
        Escala el rectángulo por un porcentaje dado.

        Parameters
        ----------
        percentage : float
            El porcentaje para escalar el rectángulo.

        Raises
        ------
        ValueError
            Si el porcentaje es menor o igual a cero.
        """
        # Verifica que el porcentaje sea positivo antes de escalar.
        if percentage <= 0:
            raise ValueError("El porcentaje de escalado tiene que ser positivo")
        self.length *= percentage / 100.0
        self.width *= percentage / 100.0

    def clone(self):
        """
        Crea y devuelve una copia de este rectángulo.

        Returns
        -------
        Rectangle
            Una copia del rectángulo.
        """
        return Rectangle(self.position.__copy__(), self.angle, self.length, self.width)

    def __str__(self):
        """
        Devuelve una representación en cadena del rectángulo.

        Returns
        -------
        str
            Una cadena que representa el rectángulo.
        """
        return f"{super().__str__()}, length={self.length}, width={self.width}"

    def __eq__(self, other):
        """
        Comprueba la igualdad con otro rectángulo.

        Parameters
        ----------
        other : Rectangle
            El objeto con el que comparar.

        Returns
        -------
        bool
            True si los rectángulos son iguales, False en caso contrario.
        """
        return isinstance(other, Rectangle) and super().__eq__(other) and self.length == other.length and self.width == other.width


