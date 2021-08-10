



class Employee():
    def __init__(self, name, adress, category, id) -> None:
        self.name = name
        self.adress = adress
        self.category = category
        self.id = id

class HoulyEmployee(Employee):
    def __init__(self, name, adress, category, id, wage) -> None:
        super().__init__(name, adress, category, id)
        self.wage = wage
        self.workedtime = 0

class CommissionedEmployee(Employee):
    def __init__(self, name, adress, category, id, salary, commission) -> None:
        super().__init__(name, adress, category, id)
        self.salary = salary
        self.commission = commission

class SalaryEmployee(Employee):
    def __init__(self, name, adress, category, id, salary) -> None:
        super().__init__(name, adress, category, id)
        self.salary = salary
