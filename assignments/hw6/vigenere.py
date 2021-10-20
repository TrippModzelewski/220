"""
Name: Tripp Modzelewski
vigenere.py

Problem: This program encrypts a message

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from graphics import GraphWin, Text, Entry, Rectangle, Point


def code(message, keyword):
    message2 = message.upper()
    message3 = message2.replace(' ', '')
    key2 = keyword.upper()
    key3 = key2.replace(' ', '')

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(keyword) >= len(message3):
        acc = ''
        for i in range(len(message3)):
            mi1 = alphabet.find(message3[i])
            ki1 = alphabet.find(key3[i])
            results = mi1 + ki1
            nu_results = alphabet[results]
            acc = acc + nu_results
        print(acc)
        return acc
    if len(keyword) < len(message3):
        key32 = key3 * 30
        acc = ''
        for i in range(len(message3)):
            mi2 = alphabet.find(message3[i])
            ki2 = alphabet.find(key32[i])
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
    keyword = key_entry.getText()

    acc = code(message, keyword)

    button.undraw()
    button_text.setText("Resulting message: ")
    result_text = Text(Point(5, 4), acc)
    result_text.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
