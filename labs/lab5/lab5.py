"""
Name: TrippModzelewski
lab5.py


Problem: This program will work with graphics

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import *
import math


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    point1 = win.getMouse()
    point1.draw(win)
    point2 = win.getMouse()
    point2.draw(win)
    point3 = win.getMouse()
    point3.draw(win)
    tri = Polygon(point1, point2, point3)
    tri.draw(win)
    tri.setFill("pink")

    x1 = point1.getX()
    x2 = point2.getX()
    x3 = point3.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    y3 = point3.getY()
    s1dx = abs(x1 - x2)
    s1dy = abs(y1 - y2)
    s2dx = abs(x2 - x3)
    s2dy = abs(y2 - y3)
    s3dx = abs(x3 - x1)
    s3dy = abs(y3 - y1)
    s1 = math.sqrt((s1dx ** 2) + (s1dy ** 2))
    s2 = math.sqrt((s2dx ** 2) + (s2dy ** 2))
    s3 = math.sqrt((s3dx ** 2) + (s3dy ** 2))

    s = (s1 + s2 + s3) / 2
    area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

    text = Text(Point(250, 400), "Area: " + str(area))
    text.draw(win)
    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''
    Create code to allow a user to color a shape by entering rgb amounts
    '''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_entry = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_entry = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_entry = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    red_entry.draw(win)
    green_entry.draw(win)
    blue_entry.draw(win)

    # Wait for another click to exit
    win.getMouse()

    for i in range(5):
        red_num = red_entry.getText()
        red_num = int(red_num)
        green_num = green_entry.getText()
        green_num = int(green_num)
        blue_num = red_entry.getText()
        blue_num = int(blue_num)

        color = color_rgb(red_num, green_num, blue_num)
        shape.setFill(color)
        win.getMouse()

    win.getMouse()
    win.close()


def process_string():
    string = input("enter string")
    print(string[0])
    print(string[-1])
    print(string[2:5])
    print(string[0] + string[-1])
    print(string[0:3] * 10)
    for i in range(len(string)):
        print(string[i])
    print(len(string))


def list_processing():
    pt = (5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    print(values[1] + values[3])
    print(values[0] + values[2])
    print(values[1] * 5)
    print(values[2:5])
    print([values[2], values[3], values[0]])
    print([values[2], values[0], float(values[5])])
    print(values[2] + values[0] + float(values[5]))
    print(len(values))


def another_series():
    n = eval(input("number of terms"))
    acc = 0
    for i in range(n):
        y = 2 + (2 * (i % 3))
        print(y, end=" ")
        acc = acc + y
    print(acc)


def main():
    # target()
    triangle()
    color_shape()
    process_string()
    list_processing()
    another_series()
    pass


main()
