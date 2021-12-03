"""
Name: Tripp Modzelewski
sales_person.py

Problem: This program creates a sales person

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


class SalesPerson:
    """SalesPerson class encapsulates data for a sales person"""

    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, nu_name):
        self.name = nu_name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        acc = 0
        for sale in self.sales:
            acc = acc + sale
        return acc

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return bool(self.total_sales() >= quota)

    def compare_to(self, other):
        if self.total_sales() > other.total_sales():
            return 1
        if self.total_sales() < other.total_sales():
            return -1
        if self.total_sales() == other.total_sales():
            return 0

    def __str__(self):
        return str(bytes(self.employee_id),  self.name,  self.total_sales())
