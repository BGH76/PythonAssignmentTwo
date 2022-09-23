
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width

    def display_data(self):
        return "Length: " + str(self.length) +\
               "\nWidth: " + str(self.width) +\
               "\nPerimeter: " + str(self.calculate_perimeter()) +\
               "\nArea: " + str(self.calculate_area())