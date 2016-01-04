from graphics import *


class Tile:
    def __init__(self, x, y, length, height, value="o"):
        self.x = x
        self.y = y
        self.pos_x = length * x
        self.pos_y = height * y
        self.value = value
        self.shape = Rectangle(Point(self.pos_x, self.pos_y), Point(self.pos_x + length, self.pos_y + height))
        self.shape.setFill("white")
        self.shape.setOutline("black")

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return str(self.value)

    def update_colour(self):
        if self.value == "x":
            self.shape.setFill("black")
            self.shape.setOutline("white")
        elif self.value == "*":
            self.shape.setFill("green")
            self.shape.setOutline("black")
        elif self.value == "S":
            self.shape.setFill("blue")
            self.shape.setOutline("black")
        elif self.value == "E":
            self.shape.setFill("red")
            self.shape.setOutline("black")
        else:
            self.shape.setFill("white")
            self.shape.setOutline("black")

    def get_shape(self):
        return self.shape
