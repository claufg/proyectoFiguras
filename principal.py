from Circle import Circle
from Square import Square
from Rectangle import Rectangle
from Coordinate import Coordinate
from Canvas import Canvas
from Exporter import CanvasXMLExport
from Exporter import CanvasJSONExport
from Exporter import CanvasTkinterExport

def main():
    """
    Función principal para ejecutar el programa interactivo del lienzo.

    Esta función inicializa un lienzo y proporciona un bucle interactivo para añadir
    diferentes formas geométricas al lienzo basado en la entrada del usuario. Soporta
    la exportación del lienzo a XML, JSON y una ventana gráfica de Tkinter.

    Parámetros
    ----------
    Ninguno

    Devoluciones
    -------
    Ninguno
    """
    # Inicializa un nuevo lienzo con un título y dimensiones específicas.
    canvas = Canvas("Mi Lienzo", 1024, 768)

    # Bucle interactivo para la manipulación del lienzo
    while True:
        # Mostrar opciones de menú al usuario
        print("Menú:")
        print("1. Agregar Círculo")
        print("2. Agregar Rectángulo")
        print("3. Agregar Cuadrado")
        print("4. Salir")
        choice = input("Ingresa tu elección: ")

        # Manejar la entrada del usuario para agregar formas o salir del programa
        if choice == '1':
            # Solicitar parámetros del círculo y añadir círculo al lienzo
            x = int(input("Ingresa la coordenada x para el centro del círculo: "))
            y = int(input("Ingresa la coordenada y para el centro del círculo: "))
            n = int(input("Ingresa el radio del círculo: "))
            canvas.add_form(Circle(Coordinate(x, y), n))
        elif choice == '2':
            # Solicitar parámetros del rectángulo y añadir rectángulo al lienzo
            x = int(input("Ingresa la coordenada x para la esquina superior izquierda del rectángulo: "))
            y = int(input("Ingresa la coordenada y para la esquina superior izquierda del rectángulo: "))
            width = int(input("Ingresa el ancho del rectángulo: "))
            length = int(input("Ingresa la altura del rectángulo: "))
            angle = float(input("Ingresa un ángulo: "))
            canvas.add_form(Rectangle(Coordinate(x, y), angle, length, width))
        elif choice == '3':
            # Solicitar parámetros del cuadrado y añadir cuadrado al lienzo
            x = int(input("Ingresa la coordenada x para la esquina superior izquierda del cuadrado: "))
            y = int(input("Ingresa la coordenada y para la esquina superior izquierda del cuadrado: "))
            side = int(input("Ingresa la longitud del lado del cuadrado: "))
            angle = float(input("Ingresa un ángulo: "))
            canvas.add_form(Square(Coordinate(x, y), angle, side))
        elif choice == '4':
            # Salir del bucle del programa
            break
        else:
            # Manejar opción inválida
            print("Opción inválida. Por favor, inténtalo de nuevo.")
            continue

        # Mostrar las formas actuales en el lienzo
        print("Formas agregadas al lienzo:")
        for form in canvas.forms:
            print(type(form).__name__, form.__dict__)

    # Exportar el lienzo a diferentes formatos después de salir del bucle
    xml_exporter = CanvasXMLExport()
    xml_data = xml_exporter.export(canvas)
    print("Exportación XML:")
    print(xml_data)

    json_exporter = CanvasJSONExport()
    json_data = json_exporter.export(canvas)
    print("\nExportación JSON:")
    print(json_data)

    tkinter_exporter = CanvasTkinterExport()
    print("\nExportación Tkinter:")
    tkinter_exporter.export(canvas)

if __name__ == '__main__':
    main()








