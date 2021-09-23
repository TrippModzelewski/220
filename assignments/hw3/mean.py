"""
Name: Tripp Modzelewski
mean.py

Problem: This function will calculate mean

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
import math


def main():
    values = eval(input("how many values will be added?"))
    acc = 0
    acc2 = 0
    acc3 = 1
    for i in range(1, values + 1):
        ex = eval(input("Enter value " + str(i) + ":"))
        acc = acc + ex ** 2
        acc2 = acc2 + (1 / ex)
        acc3 = acc3 * ex
    mean = acc / values
    rms_average = math.sqrt(mean)
    print(round(rms_average, 3))
    harmonic_mean = values / acc2
    print(round(harmonic_mean, 3))
    geometric_mean = acc3 ** (1 / values)
    print(round(geometric_mean, 3))


if __name__ == "__main__":
    main()
