"""
Name: Tripp Modzelewski
button.py

Problem: This program creates a visual

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from graphics import Text


class Button:
    """Button class creates a clickable, named button"""

    def __init__(self, shape, text):
        self.shape = shape
        cen = shape.getCenter()
        self.text = Text(cen, text)

    def set_label(self, label):
        self.text.setText(label)

    def get_label(self):
        return self.text.getText()

    def draw(self, window):
        self.shape.draw(window)
        self.text.draw(window)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def color_button(self, color):
        self.shape.setFill(color)

    def is_clicked(self, point):
        point_y = point.getY()
        point_x = point.getX()
        rec_p1 = self.shape.getP1()
        rec_p2 = self.shape.getP2()
        rec_x1 = rec_p1.getX()
        rec_x2 = rec_p2.getX()
        rec_y1 = rec_p1.getY()
        rec_y2 = rec_p2.getY()
        return bool(rec_y1 <= point_y <= rec_y2 and rec_x1 <= point_x <= rec_x2)
