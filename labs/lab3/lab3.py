"""
Name: Tripp Modzelewski
loops.py

Problem: This program uses loops to solve arithmetic problems

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def average():
    x = eval(input("How many grades are being averaged?"))
    acc = 0
    for i in range(1, x + 1):
        y = eval(input("enter grade for HW" + str(i)))
        acc = acc + y
    print(acc / x)


def tip_jar():
    acc = 0
    for i in range(1, 6):
        x = eval(input("How much would you like to donate, person " + str(i) + "?"))
        acc = acc + x
    print(acc, "dollars")


def newton():
    x = eval(input("What number would you like to take the square root of?"))
    refine = eval(input("How many times would you like to improve the approximation?"))
    approx = x / 2
    for i in range(1, refine):
        approx = (approx + (x / approx)) / 2
    print(approx)


def sequence():
    num_of_terms = eval(input("How many terms would you like to have in the series?"))
    for i in range(1, num_of_terms + 1):
        x = (1 + ((i//2) * 2))
        print(x, end=" ")


def pi():
    n = eval(input("How many terms in the series?"))
    acc = 1
    for x in range(n):
        y = (1 + (((x + 1) // 2) * 2))
        z = (2 + ((x // 2) * 2))
        frac = z / y
        acc = acc * frac
    print(acc * 2)


average()
tip_jar()
newton()
sequence()
pi()
