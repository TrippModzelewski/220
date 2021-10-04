"""
Name: Tripp Modzelewski
lab6.py


Problem: This program will work with strings

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter name, first then last: ")
    name_list = name.split(' ')
    print(name_list[1], ",", name_list[0])


def company_name():
    website = input("enter three part website name: ")
    web_split = website.split('.')
    print(web_split[1])


def initials():
    for i in range(3):
        first = input("Enter first name of student " + str(i + 1) + ": ")
        last = input("Enter " + first + "'s last name: ")
        the_initials = first[0] + last[0]
        print(first + "'s initials are: ", the_initials)


def names():
    name_string = input("Enter people's names, separated by commas: ")
    name_list = name_string.split(', ')
    for i in name_list:
        x = i.split(' ')
        first = x[0][0]
        last = x[1][0]
        print(first + last, end=" ")


def thirds():
    sentence = input("Enter a sentence: ")
    print(sentence[2::3])


def word_average():
    sentence = input("enter a sentence and i will calculate average word length: ")
    sentence_split = sentence.split(" ")
    acc = 0
    for i in sentence_split:
        length = len(i)
        acc = acc + length
    print(acc / len(sentence_split))


def pig_latin():
    sentence = input("Enter a sentence: ")
    sen_split = sentence.split(' ')
    for i in sen_split:
        first = i[0]
        rest = i[1:]
        output = (rest + first.lower() + "ay")
        print(output, end = ' ')



def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()


main()
