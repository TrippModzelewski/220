"""
Name: Tripp Modzelewski
interest.py

Problem: This function will calculate monthly interest

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def main():
    rate = eval(input("Input the annual interest rate: "))
    days = eval(input("Input total number of days in billing cycle: "))
    previous_balance = eval(input("Input net balance shown on billing statement: "))
    payment = eval(input("Input net payment received: "))
    payment_day = eval(input("Input how many days in which the bill paid: "))
    step_1 = previous_balance * days
    step_2 = payment * (days - payment_day)
    step_3 = (step_1 - step_2)
    step_4 = (step_3 / days)
    print(round(step_4 * (rate / 1200), 2))

    if __name__ == "__main__":
        main()
