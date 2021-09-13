"""
Name: Tripp Modzelewski
interest.py

Problem: This function will calculate monthly interest

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def main():
    previous_balance = eval(input("Input net balance shown on billing statement: "))
    payment = eval(input("Input net payment received: "))
    days = eval(input("Input total number of days in billing cycle: "))
    payment_day = eval(input("Input how many days in which the bill paid: "))
    rate = eval(input("Input the monthly annual interest rate: "))
    m_interest = rate / 12
    step_1 = previous_balance * days
    step_2 = payment * (days - payment_day)
    step_3 = step_2 - step_1
    average_daily_balance = step_3 / days
    interest_charge = average_daily_balance * m_interest
    print("average monthly interest charge:", interest_charge)

    if __name__ == "__main__":
        main()
