import Rectangle

class Parallelepipede(Rectangle.Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height


    def calculate_volume(self):
        return self.calculate_area() * self.height