"""
Name: Tripp Modzelewski
lab13.py


Problem: This program will search through lists

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def is_in_binary(value, values):
    left = values[0]
    right = values[len(values) - 1]
    mid = values[len(values)//2]
    while left <= right:
        if mid == value:
            return True
        if mid < value:
            left = mid + 1
        if mid > value:
            right = mid - 1
        mid = (left + right) // 2
    return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i + 1, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]
        return values


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy


def rect_sort(rectangles):
    dictionary = {}
    areas = []
    for rectangle in rectangles:
        dictionary[calc_area(rectangle)] = rectangle
        areas.append(calc_area(rectangle))
    areas = selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = dictionary[areas[i]]
    print(rectangles)


def star_find(filename):
    file = open(filename, "r")
    signals = file.read()
    sig_split = signals.split()
    found = []
    for signal in sig_split:
        if 4000 < int(signal) < 5000:
            print(sig_split.index(signal))
            found.append(signal)
            print(found)
        if len(found) == 5:
            break
    if len(found) < 5:
        print("there were not 5 signals in this range")


def main():
    # add other function calls here
    is_in_binary()
    star_find("signals.txt")
    pass


main()
