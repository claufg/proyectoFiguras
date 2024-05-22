from Circle import Circle
from Square import Square
from Rectangle import Rectangle
from Coordinate import Coordinate
from Canvas import Canvas
from Exporter import CanvasXMLExport
from Exporter import CanvasJSONExport
from Exporter import CanvasTkinterExport

def main():
    canvas = Canvas("Mi Lienzo", 1024, 768)

    while True:
        print("Menú:")
        print("1. Agregar Círculo")
        print("2. Agregar Rectángulo")
        print("3. Agregar Cuadrado")
        print("4. Salir")
        choice = input("Ingresa tu elección: ")

        if choice == '1':
            x = int(input("Ingresa la coordenada x para el centro del círculo: "))
            y = int(input("Ingresa la coordenada y para el centro del círculo: "))
            n = int(input("Ingresa el radio del círculo: "))
            canvas.add_form(Circle(Coordinate(x, y), n))
        elif choice == '2':
            x = int(input("Ingresa la coordenada x para la esquina superior izquierda del rectángulo: "))
            y = int(input("Ingresa la coordenada y para la esquina superior izquierda del rectángulo: "))
            width = int(input("Ingresa el ancho del rectángulo: "))
            height = int(input("Ingresa la altura del rectángulo: "))
            canvas.add_form(Rectangle(Coordinate(x, y), width, height))
        elif choice == '3':
            x = int(input("Ingresa la coordenada x para la esquina superior izquierda del cuadrado: "))
            y = int(input("Ingresa la coordenada y para la esquina superior izquierda del cuadrado: "))
            side = int(input("Ingresa la longitud del lado del cuadrado: "))
            angle = float(input("Ingresa un ángulo: "))
            canvas.add_form(Square(Coordinate(x, y), angle, side))
        elif choice == '4':
            break
        else:
            print("Opción inválida. Por favor, inténtalo de nuevo.")
            continue

        print("Formas agregadas al lienzo:")
        for form in canvas.forms:
            print(type(form).__name__, form.__dict__)

    # Export canvas to XML and JSON
    xml_exporter = CanvasXMLExport()
    xml_data = xml_exporter.export(canvas)
    print("XML Export:")
    print(xml_data)

    json_exporter = CanvasJSONExport()
    json_data = json_exporter.export(canvas)
    print("\nJSON Export:")
    print(json_data)

    tkinter_exporter = CanvasTkinterExport()
    print("\nTkinter Export:")
    tkinter_exporter.export(canvas)


if __name__ == "__main__":
    main()









