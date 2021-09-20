"""
Name: Tripp Modzelewski
lab4.py


Problem: This Program uses Graphics and Accumulators

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape1 = Rectangle(Point(10, 10), Point(30, 30))
    shape1.setOutline("red")
    shape1.setFill("red")
    shape1.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape1.getCenter()  # center of circle
        shape2 = shape1.clone()

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape2.move(dx, dy)
        shape2.draw(win)
    instructions.setText("Click Again To Quit")

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    pass


window = GraphWin("Rectangles", 500, 500)
point1 = window.getMouse()
point1.draw(window)
point2 = window.getMouse()
point2.draw(window)
rec = Rectangle(point1, point2)
rec.setFill("purple")
rec.draw(window)
x1 = point1.getX()
x2 = point2.getX()
y1 = point1.getY()
y2 = point2.getY()
length = abs(y2 - y1)
width = abs(x2 - x1)
perimeter = 2 * (length + width)
area = length * width
text = Text(Point(250, 400), "Perimeter: " + str(perimeter))
text.draw(window)
text2 = Text(Point(250, 420), "Area: " + str(area))
text2.draw(window)

window.getMouse()
window.close()


def circle():
    window_ = GraphWin("Circles", 500, 500)
    _point1 = window_.getMouse()
    _point1.draw(window_)
    _point2 = window_.getMouse()
    _point2.draw(window_)
    _x1 = _point1.getX()
    _x2 = _point2.getX()
    _y1 = _point1.getY()
    _y2 = _point2.getY()
    d = math.sqrt((_x2 - _x1)**2 + (_y2 - _y1)**2)
    circ = Circle(_point1, d)
    circ.draw(window_)
    circ.setFill("blue")
    window_.getMouse()
    window_.close()


def pi2():
    acc = 0
    n = eval(input("number of terms?"))
    for i in range(n):
        numerator = 4
        denominator = 1 + 2 * i
        fraction = numerator / denominator * ((-1) ** i)
        acc = acc + fraction
    print(acc)
    print(math.pi - acc)


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
