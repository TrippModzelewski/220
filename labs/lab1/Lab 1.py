"""
Name:Tripp Modzelewski
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)


def calc_rec_area():
    length = eval(input("enter the length: "))
    width = eval(input("enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("enter the length: "))
    width = eval(input("enter the width: "))
    height = eval(input("enter the height: "))
    volume = length * width * height
    print("volume =", volume)


def shooting_percentage():
    total = eval(input("enter the total: "))
    made = eval(input("enter shots made: "))
    percentage = (made/total) * 100
    print("percentage =", percentage)


def coffee():
    pounds = eval(input("how many pounds?: "))
    costs = (10.50 * pounds) + (0.86 * pounds) + 1.50
    print("costs =", costs)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers?: "))
    miles = 1.61 * kilometers
    print("miles =", miles)


calc_area()
calc_rec_area()
calc_volume()
shooting_percentage()
coffee()
kilometers_to_miles()
