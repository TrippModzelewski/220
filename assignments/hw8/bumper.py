"""
Name: Tripp Modzelewski
bumper.py

Problem: This program creates a visual

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from random import randint
import time
import graphics
import math


def get_random(move_amount):
    integer = randint(-move_amount, move_amount)
    while integer == 0:
        integer = randint(-move_amount, move_amount)
    return integer


def get_random_color():
    color = graphics.color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return color


def hit_horizontal(circle):
    center = circle.getCenter()
    cen_y = center.getY()
    if cen_y >= 375 or cen_y <= 25:
        return True
    else:
        return False


def hit_vertical(circle):
    center = circle.getCenter()
    cen_x = center.getX()
    if cen_x >= 375 or cen_x <= 25:
        return True
    else:
        return False


def did_collide(circle1, circle2):
    cen1 = circle1.getCenter()
    cen2 = circle2.getCenter()
    center_distance = math.sqrt((cen1.getX() - cen2.getX()) ** 2 + (cen1.getY() - cen2.getY()) ** 2)
    if center_distance <= 50:
        return True
    else:
        return False


def main():
    win = graphics.GraphWin("bumper.py", 400, 400)

    circle1 = graphics.Circle(graphics.Point(randint(26, 374), randint(26, 374)), 25)
    circle2 = graphics.Circle(graphics.Point(randint(26, 374), randint(26, 374)), 25)
    circle1.draw(win)
    circle2.draw(win)
    circle1.setFill(get_random_color())
    circle2.setFill(get_random_color())
    win.setBackground(get_random_color())
    x = 0
    dx = get_random(1)
    dy = get_random(1)
    dx2 = get_random(1)
    dy2 = get_random(1)
    while x == 0:
        circle1.move(dx, dy)
        time.sleep(.000000000001)
        hit_hori = hit_horizontal(circle1)
        hit_vert = hit_vertical(circle1)
        circle2.move(dx2, dy2)
        hit_hori2 = hit_horizontal(circle2)
        hit_vert2 = hit_vertical(circle2)
        collide = did_collide(circle1, circle2)
        if hit_hori is True:
            dy = -dy
        elif hit_hori is False:
            dy = dy
        if hit_vert is True:
            dx = -dx
        elif hit_vert is False:
            dx = dx

        if hit_hori2 is True:
            dy2 = -dy2
        elif hit_hori2 is False:
            dy2 = dy2
        if hit_vert2 is True:
            dx2 = -dx2
        elif hit_vert2 is False:
            dx2 = dx2

        if collide is True:
            dx = -dx
            dy = -dy
            dx2 = -dx2
            dy2 = -dy2
        elif collide is False:
            dx = dx
            dy = dy
            dx2 = dx2
            dy2 = dy2

    win.close()


main()
