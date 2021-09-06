"""
Name: Tripp Modzelewski
lab2.py

Problem: This program does arithmetic

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

import math


def sum_of_threes():
    upper_bound = eval(input("Upper bound?"))

    def addition():
        acc = 0
        for i in range(0, upper_bound + 1, 3):
            acc = acc + i
        print(acc)

    print("sum equals", addition())


def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(l * h, end=" ")
        print()


def triangle_area():
    x = eval(input("length of side 1"))
    y = eval(input("length of side 2"))
    z = eval(input("length of side 3"))
    s = (x + y + z) / 2
    a = math.sqrt(s * (s - x) * (s - y) * (s - z))
    print("area equals", a)


def sum_squares():
    x = eval(input("Lower Bound?"))
    y = eval(input("Upper Bound?"))
    acc = 0
    for i in range(x, y + 1):
        acc = acc + (i * i)
    print(acc)


def power():
    base = eval(input("enter the desired base"))
    exponent = eval(input("enter the desired exponent"))
    acc = 1
    for x in range(exponent):
        acc = acc * base
    print(acc)


sum_of_threes()
multiplication_table()
triangle_area()
sum_squares()
power()
