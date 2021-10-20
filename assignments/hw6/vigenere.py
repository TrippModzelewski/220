"""
Name: Tripp Modzelewski
vigenere.py

Problem: This program encrypts a message

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from graphics import GraphWin, Text, Entry, Rectangle, Point


def code(message, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(keyword) >= len(message):
        acc = ''
        for i in range(len(message)):
            mi1 = alphabet.find(message[i])
            ki1 = alphabet.find(keyword[i])
            results = mi1 + ki1
            nu_results = alphabet[results]
            acc = acc + nu_results
        print(acc)
        return acc
    if len(keyword) < len(message):
        keyword2 = keyword * 30
        acc = ''
        for i in range(len(message)):
            mi2 = alphabet.find(message[i])
            ki2 = alphabet.find(keyword2[i])
            results2 = mi2 + ki2
            new_res = alphabet[results2]
            acc = acc + new_res
        print(acc)
        return acc


def main():
    win = GraphWin("Vigenere", 500, 400)
    win.setCoords(0, 0, 10, 10)
    message_text = Text(Point(2, 9), "Message to encrypt: ")
    message_text.draw(win)
    message_entry = Entry(Point(6, 9), 25)
    message_entry.draw(win)
    key_text = Text(Point(2.3, 7), "Enter keyword: ")
    key_text.draw(win)
    key_entry = Entry(Point(6, 7), 25)
    key_entry.draw(win)
    button = Rectangle(Point(4, 4), Point(6, 5))
    button.draw(win)
    button_text = Text(Point(5, 4.5), "Encode")
    button_text.draw(win)

    win.getMouse()

    message = message_entry.getText()
    message2 = message.upper()
    message3 = message2.replace(' ', '')
    key = key_entry.getText()
    key2 = key.upper()
    key3 = key2.replace(' ', '')

    acc = code(message3, key3)

    button.undraw()
    button_text.setText("Resulting message: ")
    result_text = Text(Point(5, 4), acc)
    result_text.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
