from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET
from Circle3D import Circle3D
from Square3D import Square3D
from Rectangle3D import Rectangle3D
import tkinter as tk

class Exporter(ABC):
    @abstractmethod
    def export(self, shapes, filename):
        pass

class CanvasJSONExport(Exporter):
    def export(self, shapes, filename):
        data = [{"type": shape.__class__.__name__, "position": shape.get_position().tolist(), "properties": shape.__dict__} for shape in shapes]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

class CanvasXMLExport(Exporter):
    def export(self, shapes, filename):
        root = ET.Element("shapes")
        for shape in shapes:
            shape_elem = ET.SubElement(root, shape.__class__.__name__)
            position = shape.get_position()
            ET.SubElement(shape_elem, "position").text = str(position.tolist())
            for key, value in shape.__dict__.items():
                if key != 'position':
                    ET.SubElement(shape_elem, key).text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename)

class CanvasTkinterExport(Exporter):
    def export(self, shapes, filename):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=800, height=600)
        canvas.pack()

        for shape in shapes:
            position = shape.get_position()
            if isinstance(shape, Circle3D):
                x, y, z = position
                r = shape.get_radius()
                canvas.create_oval(x-r, y-r, x+r, y+r, outline="black")
            elif isinstance(shape, Rectangle3D):
                x, y, z = position
                w, h = shape.get_dimensions()
                canvas.create_rectangle(x, y, x+w, y+h, outline="black")
            elif isinstance(shape, Square3D):
                x, y, z = position
                s = shape.get_side_length()
                canvas.create_rectangle(x, y, x+s, y+s, outline="black")

        canvas.update()
        canvas.postscript(file=filename + ".ps")
        root.destroy()
