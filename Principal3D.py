from Circle3D import Circle3D
from Square3D import Square3D
from Rectangle3D import Rectangle3D
from Canvas import Canvas
from Exporter import CanvasJSONExport, CanvasXMLExport, CanvasTkinterExport

def main():
    circle = Circle3D(5, [1, 2, 3])
    square = Square3D(4, [4, 5, 6])
    rectangle = Rectangle3D(3, 6, [7, 8, 9])

    canvas = Canvas()
    canvas.add_shape(circle)
    canvas.add_shape(square)
    canvas.add_shape(rectangle)

    print(circle)
    print(square)
    print(rectangle)

    canvas.draw()

    json_exporter = CanvasJSONExport()
    json_exporter.export(canvas.shapes, 'shapes.json')

    xml_exporter = CanvasXMLExport()
    xml_exporter.export(canvas.shapes, 'shapes.xml')

    tkinter_exporter = CanvasTkinterExport()
    tkinter_exporter.export(canvas.shapes, 'shapes')

if __name__ == "__main__":
    main()
