"""
Name: Tripp Modzelewski
lab9.py


Problem: This program will work with conditionals

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


from graphics import *
import math


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10
    print(nums)


def square_each(nums):
    print(nums)
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums


def sum_list(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])
    return nums


def writesumofsquares():
    infile = input("enter input file name: ")
    outfile = input("enter output file name: ")
    readfile = open(infile, 'r')
    writefile = open(outfile, 'w+')
    for line in readfile:
        nums = line.split(' ')
        to_numbers(nums)
        square_each(nums)
        summation = sum_list(nums)
        writefile.write("sum of squares = " + str(summation))


def starter():
    weight = eval(input("enter weight: "))
    wins = eval(input("enter amount of wins: "))
    if 150 <= weight <= 160 and wins >= 5:
        print("is a starter")
    elif weight >= 199 and wins >= 20:
        print("is a starter")
    else:
        print("is not a starter")


def leap_year(year):
    c1 = year % 4
    c2 = year % 100
    c3 = year % 400
    if c1 == 0 and (c2 != 0 or c3 == 0):
        return True
    else:
        return False


def circleoverlap():
    win = GraphWin("circle shit", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, radius1)
    c1.draw(win)
    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, radius2)
    c2.draw(win)
    center_distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    if center_distance <= (radius1 + radius2):
        text = Text(Point(200, 300), "circles overlap")
        text.draw(win)
    else:
        text = Text(Point(200, 300), "circles do not overlap")
        text.draw(win)

    win.getMouse()
    win.close()



def main():
    # add other function calls here
    # add_ten([5, 2, -3])
    # writesumofsquares()
    # starter()
    # leap_year(2000)
    pass


main()
