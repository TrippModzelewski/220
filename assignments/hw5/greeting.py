"""
Name: Tripp Modzelewski
greeting.py

Problem: This program creates a greeting card

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


import time
from graphics import GraphWin, Circle, Polygon, Point, Text, Line


def main():
    win = GraphWin("Greeting Card", 500, 500)

    # create heart
    point1 = Point(150, 150)
    point2 = Point(350, 150)
    point3 = Point(62, 200)
    point4 = Point(437.5, 200)
    point5 = Point(250, 400)
    point6 = Point(250, 150)
    circle1 = Circle(point1, 100)
    circle1.draw(win)
    circle2 = Circle(point2, 100)
    circle2.draw(win)
    triangle = Polygon(point3, point6, point4, point5)
    triangle.draw(win)
    circle1.setFill("red")
    circle2.setFill("red")
    triangle.setFill("red")
    triangle.setOutline("red")
    circle1.setOutline("red")
    circle2.setOutline("red")
    nother_point = Point(310, 190)
    circle3 = Circle(nother_point, 70)
    circle3.setFill("red")
    circle3.setOutline("red")

    # text
    point = Point(250, 450)
    text = Text(point, "Happy Valentines Day!")
    text.draw(win)

    # create arrow
    point7 = Point(0, 500)
    point8 = Point(150, 350)
    line1 = Line(point7, point8)
    line1.draw(win)
    poi1 = Point(150, 350)
    poi2 = Point(130, 360)
    poi3 = Point(140, 360)
    poi4 = Point(142.5, 370)
    arrowhead = Polygon(poi1, poi2, poi3, poi4)
    arrowhead.draw(win)
    arrowhead.setFill("black")
    po1 = Point(0, 500)
    po2 = Point(0, 510)
    line2 = Line(po1, po2)
    line2.draw(win)
    po3 = Point(10, 490)
    po4 = Point(10, 500)
    line3 = Line(po3, po4)
    line3.draw(win)
    po5 = Point(0, 490)
    line4 = Line(po3, po5)
    line4.draw(win)
    po6 = Point(-10, 500)
    line5 = Line(po6, po1)
    line5.draw(win)
    circle3.draw(win)

    # Movement
    for _ in range(200):
        arrowhead.move(1, -1)
        line1.move(1, -1)
        line2.move(1, -1)
        line3.move(1, -1)
        line4.move(1, -1)
        line5.move(1, -1)
        time.sleep(.01)
    text.setText("Click anywhere to close...")

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
