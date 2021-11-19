"""
Name: Tripp Modzelewski
button.py

Problem: This program creates a visual

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from graphics import *


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = label

    def set_label(self, name):
        self.text = name

    def get_label(self):
        return self.text

    def draw(self, window):
        self.shape.draw(window)
        self.text.draw(window)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def color_button(self, color):
        self.shape.setFill(color)

    def is_clicked(self, point):
        y = point.getY()
        x = point.getX()
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        x1 = p1.getX()
        x2 = p2.getX()
        y1 = p1.getY()
        y2 = p2.getY()
        if y1 <= y <= y2 and x1 <= x <= x2:
            return True
        else:
            return False
