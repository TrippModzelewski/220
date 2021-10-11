"""
Name: Tripp Modzelewski
lab6.py


Problem: This program will work with functions and Spy Craft(?)

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
import math


def cash_conversion():
    x = eval(input("Enter an integer: "))
    print('${: .2f}'.format(x))


def encode():
    x = input("Enter a secret message: ")
    k = eval(input("Enter an integer: "))
    acc = ""
    for i in range(len(x)):
        n = ord(x[i])
        s = n + k
        secret_character = chr(s)
        acc = acc + secret_character
    print(acc)


def sphere_area(radius):
    area = 4 * math.pi * radius ** 2
    return area


def sphere_volume(radius):
    volume = (4/3) * math.pi * radius ** 2
    return volume


def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        c = i ** 3
        acc = acc + c
    return acc


def encode_better():
    m = input("enter a message you would like to keep secret: ")
    k = input("enter a key: ")
    acc = ""
    for i in range(len(m)):
        mi = ord(m[i])
        ki = ord(k[i])
        result = mi + ki - 97
        acc = acc + chr(result)
    print(acc)


def main():
    # add function calls her
    cash_conversion()
    encode()
    print("surface area =", sphere_area(2))
    print("volume =", sphere_volume(5))
    print("sum =", sum_n(10))
    print("sum =", sum_n_cubes(10))
    encode_better()
    pass


main()