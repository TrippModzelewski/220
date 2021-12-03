"""
Name: Tripp Modzelewski
sales_force.py

Problem: This program creates a work force

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from sales_person import SalesPerson


class SalesForce:
    """ SalesForce encapsulates the data of all collected salespeople"""

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        text = open(file_name, 'r')
        data = text.readlines()
        for line in data:
            self.sales_people.append(line)

    def quota_report(self, quota):
        nu_list = []
        for item in self.sales_people:
            tot_sales = 0
            data_split = item.split(', ')
            data_split[0] = int(data_split[0])
            sales = data_split[2].split(' ')
            for sale in sales:
                tot_sales = tot_sales + sale
            x = bool(tot_sales >= quota)
            nu_list.append([data_split[0], data_split[1], tot_sales, x])

    def top_seller(self):
        tot_list = []
        for item in self.sales_people:
            tot_sales = 0
            data_split = item.split(', ')
            data_split[0] = int(data_split[0])
            sales = data_split[2].split(' ')
            for sale in sales:
                tot_sales = tot_sales + sale


    def individual_sales(self, employee_id):
        pass

