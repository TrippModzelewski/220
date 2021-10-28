"""
Name: Tripp Modzelewski
weighted_average.py

Problem: This program calculates weighted average

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

# Sorry it was late, I did not realize it was due on Tuesday
# and I had 2 tests today, so I could not get it done yesterday.
# But it's done and it's beautiful. See you tomorrow.


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w+')
    for line in infile:
        acc = 0
        name_from_num = line.split(': ')
        numbers = name_from_num[1].split(' ')
        name = name_from_num[0]

        w = numbers[::2]
        g = numbers[1::2]

        acc2 = 0
        for i in range(len(g)):
            xini = int(w[i]) * int(g[i])
            acc = acc + xini
            acc2 = acc2 + int(w[i])
        if acc2 == 100:
            answer = round(acc / 100, 1)
        elif acc2 > 100:
            answer = "Error: The weights are more than 100."
        else:
            answer = "Error: The weights are less than 100."

        outfile.write(name + "'s average: " + str(answer) + "\n")


if __name__ == '__main__':
    weighted_average("grades.txt", "avg.txt")
