"""
Name: Tripp Modzelewski
bumper.py

Problem: This program creates a visual

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
import math
from random import randint
import time
import graphics


def get_random(move_amount):
    integer = randint(-move_amount, move_amount)
    while integer == 0:
        integer = randint(-move_amount, move_amount)
    return integer


def get_random_color():
    color = graphics.color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return color


def hit_horizontal(circle, win):
    center = circle.getCenter()
    cen_y = center.getY()
    rad = circle.getRadius()
    height = win.winfo_height()
    return bool(cen_y >= height - rad or cen_y <= rad)


def hit_vertical(circle, win):
    center = circle.getCenter()
    cen_x = center.getX()
    rad = circle.getRadius()
    width = win.winfo_width()
    return bool(cen_x >= width - rad or cen_x <= rad)


def did_collide(circle1, circle2):
    cen1 = circle1.getCenter()
    cen2 = circle2.getCenter()
    rad1 = circle1.getRadius()
    rad2 = circle2.getRadius()
    center_distance = math.sqrt((cen1.getX() - cen2.getX()) ** 2 + (cen1.getY() - cen2.getY()) ** 2)
    return bool(center_distance <= rad1 + rad2)


def main():
    win = graphics.GraphWin("bumper.py", 400, 400)

    circle1 = graphics.Circle(graphics.Point(randint(26, 374), randint(26, 374)), 25)
    circle2 = graphics.Circle(graphics.Point(randint(26, 374), randint(26, 374)), 25)
    circle1.draw(win)
    circle2.draw(win)
    circle1.setFill(get_random_color())
    circle2.setFill(get_random_color())
    win.setBackground(get_random_color())
    xini = 0
    dx1 = get_random(1)
    dy1 = get_random(1)
    dx2 = get_random(1)
    dy2 = get_random(1)
    while xini == 0:
        circle1.move(dx1, dy1)
        time.sleep(.000000000001)
        hit_hori = hit_horizontal(circle1, win)
        hit_vert = hit_vertical(circle1, win)
        circle2.move(dx2, dy2)
        hit_hori2 = hit_horizontal(circle2, win)
        hit_vert2 = hit_vertical(circle2, win)
        collide = did_collide(circle1, circle2)
        if hit_hori is True:
            dy1 = -dy1
        elif hit_hori is False:
            pass
        if hit_vert is True:
            dx1 = -dx1
        elif hit_vert is False:
            pass

        if hit_hori2 is True:
            dy2 = -dy2
        elif hit_hori2 is False:
            pass
        if hit_vert2 is True:
            dx2 = -dx2
        elif hit_vert2 is False:
            pass

        if collide is True:
            dx1 = -dx1
            dy1 = -dy1
            dx2 = -dx2
            dy2 = -dy2
        elif collide is False:
            pass

    win.close()


if __name__ == '__main__':
    main()
