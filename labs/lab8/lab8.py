"""
Name: Tripp Modzelewski
lab8.py


Problem: This program will work with functions

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w+')
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(str(i) + " " + word + "\n")
            i = i + 1
    infile.close()
    outfile.close()


def hourly_wage(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w+')
    for line in infile:
        parts = line.split(' ')
        wage = float(parts[2])
        wage = wage + 1.65
        wage = wage * int(parts[3])
        outfile.write(parts[0] + " " + parts[1] + " " + str(wage) + "\n")


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        position = 10 - i
        acc = acc + int(isbn[i]) * position
    print(acc)
    return acc


def send_message(file, friend):
    infile = open(file, 'r')
    outfile = open(friend + ".txt", 'w+')
    text = infile.read()
    outfile.write(text)


def send_safe_message(file, friend, key):
    infile = open(file, 'r')
    outfile = open(friend + ".txt", 'w+')
    text = infile.read()
    outfile.write(encode(text, key))


def send_uncrackable_message(file, friend, pad):
    infile = open(file, 'r')
    outfile = open(friend + ".txt", 'w+')
    padtext = open(pad, 'r')
    text = infile.read()
    outfile.write(encode_better(text, padtext.read()))


def main():
    number_words("Walrus.txt", "output1.txt")
    hourly_wage("hourly_wages.txt", "output2.txt")
    calc_check_sum("0072946520")
    send_message("message.txt", "Derrick")
    send_safe_message("secret_message.txt", "Dennis", 3)
    send_uncrackable_message("safest_message.txt", "Don", "pad.txt")
    pass


main()
