"""
Name: Tripp Modzelewski
lab12.py


Problem: This program will loop through lists

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from random import randint


def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Tripp"
    except ValueError:
        pass


def read_data(filename):
    f = open(filename, 'r')
    data = f.read()
    data = data.split()
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == values[i]:
            return True
        i = i + 1
    return False


def good_input():
    x = eval(input("enter a value between 1 and 10: "))
    while x <= 1 or x >= 10:
        x = eval(input("that was not in between 1 and 10, please try again: "))
    return x


def num_digits():
    num = eval(input("enter a positive value to see how many digits it has! enter 0 or a negative to exit!"))
    while num != 0:
        digits = 0
        while num != 0:
            num = num // 10
            digits = digits + 1
        print(digits, "digits")
        num = eval(input("enter a positive value to see how many digits it has!enter 0 or negative to exit!"))


def hi_lo_game():
    secret = randint(1, 100)
    guess = 1
    num = eval(input("guess my secret number"))
    while guess <= 7 and num != secret:
        guess = guess + 1
        if num < secret:
            print("guess higher")
        else:
            print("guess lower")
        num = eval(input("guess again!"))
    if num != secret:
        print("you lose, my secret number was", secret)
    else:
        print("you won! you got my secret number")


def main():
    # add other function calls here
    find_and_remove_first([1, 2, 3, 4], 4)
    is_in_linear("4", read_data("text.txt"))
    good_input()
    num_digits()
    hi_lo_game()


main()
