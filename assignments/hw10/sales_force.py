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
            split = line.split(', ')
            nu_addition = SalesPerson(split[0], split[1])
            self.sales_people.append(nu_addition)
            trying = split[2].strip("\n")
            sales = trying.split(' ')
            for sale in sales:
                nu_addition.enter_sale(sale)

    def quota_report(self, quota):
        nu_list = []
        for item in self.sales_people:
            nu_list.append([SalesPerson.get_id(item), SalesPerson.get_name(item), SalesPerson.total_sales(item), SalesPerson.met_quota(item, quota)])
        return nu_list

    def top_seller(self):
        space_filler = SalesPerson(-1, "empty")
        space_filler.enter_sale(0)
        lst = [space_filler]
        for item in self.sales_people:
            if item.total_sales() > lst[0].total_sales():
                lst = []
                lst.append(item)
            if item.total_sales() == lst[0].total_sales():
                lst.append(item)

    def individual_sales(self, employee_id):
        for item in self.sales_people:
            if item.get_id == employee_id:
                return item
        return None
