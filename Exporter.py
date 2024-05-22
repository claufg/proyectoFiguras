from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET
from Circle import Circle
from Square import Square
from Rectangle import Rectangle
import tkinter as tk

class CanvasExport(ABC):
    @abstractmethod
    def export(self, canvas):
        pass

class CanvasXMLExport(CanvasExport):
    def export(self, canvas):
        root = ET.Element("canvas")
        title = ET.SubElement(root, "title")
        title.text = canvas.title
        dimensions = ET.SubElement(root, "dimensions")
        dimensions.set("width", str(canvas.width))
        dimensions.set("height", str(canvas.height))
        forms = ET.SubElement(root, "forms")
        for form in canvas.forms:
            form_element = ET.SubElement(forms, form.__class__.__name__)
            position = ET.SubElement(form_element, "position")
            position.set("x", str(form.position.x))
            position.set("y", str(form.position.y))
            if isinstance(form, Circle):
                radius = ET.SubElement(form_element, "radius")
                radius.text = str(form.radius)
            elif isinstance(form, Rectangle):
                angle = ET.SubElement(form_element, "angle")
                angle.text = str(form.angle)
                length = ET.SubElement(form_element, "length")
                length.text = str(form.length)
                width = ET.SubElement(form_element, "width")
                width.text = str(form.width)
            elif isinstance(form, Square):
                angle = ET.SubElement(form_element, "angle")
                angle.text = str(form.angle)
                side = ET.SubElement(form_element, "side")
                side.text = str(form.side)
        return ET.tostring(root, encoding='unicode')

class CanvasJSONExport(CanvasExport):
    def export(self, canvas):
        canvas_dict = {
            "title": canvas.title,
            "dimensions": {
                "width": canvas.width,
                "height": canvas.height
            },
            "forms": []
        }
        for form in canvas.forms:
            form_dict = {
                "type": form.__class__.__name__,
                "position": {
                    "x": form.position.x,
                    "y": form.position.y
                }
            }
            if isinstance(form, Circle):
                form_dict["radius"] = form.radius
            elif isinstance(form, Rectangle):
                form_dict["angle"] = form.angle
                form_dict["length"] = form.length
                form_dict["width"] = form.width
            elif isinstance(form, Square):
                form_dict["angle"] = form.angle
                form_dict["side"] = form.side
            canvas_dict["forms"].append(form_dict)
        return json.dumps(canvas_dict, indent=4)


class CanvasTkinterExport(CanvasExport):
    def export(self, canvas):
        root = tk.Tk()
        root.title(canvas.title)
        tk_canvas = tk.Canvas(root, width=canvas.width, height=canvas.height, bg="white")
        tk_canvas.pack()

        for form in canvas.forms:
            if isinstance(form, Circle):
                x0 = form.position.x - form.radius
                y0 = form.position.y - form.radius
                x1 = form.position.x + form.radius
                y1 = form.position.y + form.radius
                tk_canvas.create_oval(x0, y0, x1, y1, outline="black")
            elif isinstance(form, Rectangle):
                x0 = form.position.x
                y0 = form.position.y
                x1 = x0 + form.width
                y1 = y0 + form.length
                tk_canvas.create_rectangle(x0, y0, x1, y1, outline="black")
            elif isinstance(form, Square):
                x0 = form.position.x
                y0 = form.position.y
                x1 = x0 + form.side
                y1 = y0 + form.side
                tk_canvas.create_rectangle(x0, y0, x1, y1, outline="black")

        root.mainloop()
