class Canvas:
    """
    Clase que representa un lienzo para dibujar formas.

    Attributes
    ----------
    title : str
        Título del lienzo.
    width : float
        Ancho del lienzo.
    height : float
        Altura del lienzo.
    forms : list
        Lista que almacena las formas dibujadas en el lienzo.

    Methods
    -------
    add_form(form):
        Añade una forma al lienzo.
    clone():
        Crea y devuelve una copia de este lienzo.
    get_width():
        Devuelve el ancho del lienzo.
    get_height():
        Devuelve la altura del lienzo.
    get_num_forms():
        Devuelve el número de formas en el lienzo.
    get_form(index):
        Obtiene una forma por su índice.
    remove_form(index):
        Elimina una forma del lienzo por su índice.
    __str__():
        Devuelve una representación en cadena del lienzo.
    """

    DEFAULT_SIZE = 1000.0  # Tamaño por defecto para el ancho y la altura del lienzo.

    def __init__(self, title="default canvas", width=DEFAULT_SIZE, height=DEFAULT_SIZE):
        """
        Inicializa una nueva instancia de Canvas.

        Parameters
        ----------
        title : str, optional
            Título del lienzo (default is "default canvas").
        width : float, optional
            Ancho del lienzo (default is DEFAULT_SIZE).
        height : float, optional
            Altura del lienzo (default is DEFAULT_SIZE).

        Raises
        ------
        ValueError
            Si el ancho o la altura son negativos.
        """
        if width < 0 or height < 0:
            raise ValueError("El ancho y la altura no pueden ser negativos.")
        self.title = title
        self.width = width
        self.height = height
        self.forms = []  # Lista para almacenar formas dibujadas en el lienzo.

    def add_form(self, form):
        """
        Añade una forma al lienzo.

        Parameters
        ----------
        form : Form2D
            La forma a añadir al lienzo.
        """
        self.forms.append(form)

    def clone(self):
        """
        Crea y devuelve una copia de este lienzo.

        Returns
        -------
        Canvas
            Una copia del lienzo actual.
        """
        new_canvas = Canvas(self.title, self.width, self.height)
        new_canvas.forms = [form.clone() for form in self.forms]
        return new_canvas

    def get_width(self):
        """
        Devuelve el ancho del lienzo.

        Returns
        -------
        float
            El ancho del lienzo.
        """
        return self.width

    def get_height(self):
        """
        Devuelve la altura del lienzo.

        Returns
        -------
        float
            La altura del lienzo.
        """
        return self.height

    def get_num_forms(self):
        """
        Devuelve el número de formas en el lienzo.

        Returns
        -------
        int
            El número de formas contenidas en el lienzo.
        """
        return len(self.forms)

    def get_form(self, index):
        """
        Obtiene una forma por su índice.

        Parameters
        ----------
        index : int
            El índice de la forma a obtener.

        Raises
        ------
        IndexError
            Si el índice está fuera del rango válido.

        Returns
        -------
        Form2D
            La forma en el índice especificado.
        """
        if index < 1 or index > len(self.forms):
            raise IndexError("Form index out of range")
        return self.forms[index - 1]

    def remove_form(self, index):
        """
        Elimina una forma del lienzo por su índice.

        Parameters
        ----------
        index : int
            El índice de la forma a eliminar.

        Raises
        ------
        IndexError
            Si el índice está fuera del rango válido.
        """
        if index < 1 or index > len(self.forms):
            raise IndexError("Form index out of range")
        self.forms.pop(index - 1)

    def __str__(self):
        """
        Devuelve una representación en cadena del lienzo.

        Returns
        -------
        str
            Una cadena que representa el lienzo, incluyendo su título, dimensiones y número de formas.
        """
        return f"{self.title} ({self.width},{self.height}) con {len(self.forms)} formas"

