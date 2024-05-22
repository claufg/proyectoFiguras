from Circle import Circle
from Square import Square
from Rectagle import Rectangle

class Form2DFactory:
    @staticmethod
    def create_form2d(form_type):
        if form_type == "Circle":
            return Circle()
        elif form_type == "Square":
            return Square()
        elif form_type == "Rectangle":
            return Rectangle()
        else:
            raise ValueError("Invalid form type")
