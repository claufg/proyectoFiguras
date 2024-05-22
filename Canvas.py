class Canvas:
    DEFAULT_SIZE = 1000.0

    def __init__(self, title="default canvas", width=DEFAULT_SIZE, height=DEFAULT_SIZE):
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative")
        self.title = title
        self.width = width
        self.height = height
        self.forms = []

    def add_form(self, form):
        self.forms.append(form)

    def clone(self):
        new_canvas = Canvas(self.title, self.width, self.height)
        new_canvas.forms = [form.clone() for form in self.forms]
        return new_canvas

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_num_forms(self):
        return len(self.forms)

    def get_form(self, index):
        if index < 1 or index > len(self.forms):
            raise IndexError("Form index out of range")
        return self.forms[index - 1]

    def remove_form(self, index):
        if index < 1 or index > len(self.forms):
            raise IndexError("Form index out of range")
        self.forms.pop(index - 1)

    def __str__(self):
        return f"{self.title} ({self.width},{self.height}) with {len(self.forms)} forms"

