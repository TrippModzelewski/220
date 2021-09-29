"""
Name: Tripp Modzelewski
traffic.py

Problem: This program averages the amount of cars

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def main():
    roads = eval(input("How many roads were surveyed?"))
    acc2 = 0
    for eye in range(roads):
        days = eval(input("How many days was road " + str(eye + 1) + " surveyed?"))
        acc = 0
        for i in range(days):
            cars = eval(input("How many cars traveled on day " + str(i + 1) + " ?"))
            acc = acc + cars
            acc2 = acc2 + cars
        average = acc / days
        print("Road " + str(eye + 1) + " average vehicles per day:",  round(average, 2))
    print("Total number of vehicles on all roads:", acc2)
    print("Average number of vehicles per road:", round((acc2 / roads), 2))


if __name__ == '__main__':
    main()
