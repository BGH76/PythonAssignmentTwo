
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name: " + self.name + "\n" +
              "Age: " + self.age)



class Student(Person):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def display_student(self):
        print("Name: " + self.name + "\n" +
              "Age: " + str(self.age) + "\n" +
              "Color: " + self.color)