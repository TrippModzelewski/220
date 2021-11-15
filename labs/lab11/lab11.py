"""
Name: Tripp Modzelewski
lab11.py


Problem: This program will build a hangman game

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from random import *


def words(ifn):
    infile = open(ifn, 'r')
    content = infile.readlines()
    return content


def random_word(word_list):
    return word_list[randint(0, len(word_list)-1)]


def fill(word, letters):
    # need to use strings for both guesses and word
    secret = ["_"] * (len(word) - 1)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)


def play():
    w_list = words("words.txt")
    secret = random_word(w_list)
    incorrect = 0
    guesses = []
    current = "_" * len(secret)
    if '_' in current:
        state = True
    else:
        state = False
    while state is True and incorrect < 7:
        display = fill(secret, guesses)
        print(display)
        print(guesses)
        letter = input("enter a guess:")
        while letter in guesses:
            letter = input("already guessed that! Try again:")
        guesses.append(letter)
        display = fill(secret, guesses)
        if current == display:
            incorrect = incorrect + 1
            print("incorrect guesses:", incorrect)
        else:
            current = display

        if '_' in current:
            state = True
        else:
            state = False
    if incorrect == 7:
        print("you lose, correct answer was:", secret)
    if state is False:
        print("you win")


def main():
    # add other function calls here
    play()
    pass


main()
