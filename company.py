from random import randint

class Company():
    employees = {}

    @staticmethod
    def generate_new_id():
        id = 0
        while id in Company.employees:
            id = randint(0,499)
        return id

    @classmethod
    def add_employee(cls, employee):
        cls.employees[employee.id] = employee

    @classmethod
    def remove_employee(cls, id):
        del cls.employees[id]
