"""
Name: Tripp Modzelewski
three_door_game.py

Problem: This program creates a three door game

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from random import randint
from graphics import GraphWin, Point, Rectangle, Text
from button import Button


def main():
    win = GraphWin("Three Door Game", 500, 500)
    win.setCoords(0, 0, 19, 19)
    door1 = Button(Rectangle(Point(1, 8), Point(6, 12)), "door 1")
    door1.draw(win)
    door2 = Button(Rectangle(Point(7, 8), Point(12, 12)), "door 2")
    door2.draw(win)
    door3 = Button(Rectangle(Point(13, 8), Point(18, 12)), "door 3")
    door3.draw(win)
    top_txt = Text(Point(9.5, 17), "I have a secret door")
    top_txt.draw(win)
    bottom_txt = Text(Point(9.5, 3), "Click to choose a door")
    bottom_txt.draw(win)
    rand = randint(1, 3)
    point = win.getMouse()
    if door1.is_clicked(point) is True:
        ans = 1
        if rand == ans:
            door1.color_button("green")
            top_txt.setText("You Win!")
            bottom_txt.setText("Click To Close")
        else:
            door1.color_button("red")
            top_txt.setText("You Lose!")
            bottom_txt.setText("Door " + str(rand) + " was my secret door")
    if door2.is_clicked(point) is True:
        ans = 2
        if rand == ans:
            door2.color_button("green")
            top_txt.setText("You Win!")
            bottom_txt.setText("Click To Close")
        else:
            door2.color_button("red")
            top_txt.setText("You Lose!")
            bottom_txt.setText("Door " + str(rand) + " was my secret door")
    if door3.is_clicked(point) is True:
        ans = 3
        if rand == ans:
            door3.color_button("green")
            top_txt.setText("You Win!")
            bottom_txt.setText("Click To Close")
        else:
            door3.color_button("red")
            top_txt.setText("You Lose!")
            bottom_txt.setText("Door " + str(rand) + " was my secret door")

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
