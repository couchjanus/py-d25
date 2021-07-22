# базовый класс Employee, 

from hr.prs import (
    SalaryPolicy,
    CommissionPolicy,
    HourlyPolicy
)
from hr.productivity import (
    ManagerRole,
    SecretaryRole,
    SalesRole,
    FactoryRole
)

# Другим атрибутом для Employee может быть Address:
# можно добавить Address в класс Employee с помощью композиции:
class Employee:
    def __init__(self, id, name):
        self.id = id # id для идентификации сотрудника.
        self.name = name # name, содержащее имя сотрудника.
        self.address = None

# Мы инициализируем атрибут address значением None на данный момент, 
# чтобы сделать его необязательным, но, сделав это, теперь можно назначить Address для Employee. 
# Также обратите внимание, что в модуле employee нет ссылки на модуль contacts.

# Композиция – это слабо связанные отношения, которые часто не требуют, 
# чтобы составной класс обладал знаниями о компоненте.

class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)

class Secretary(Employee, SecretaryRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)

class SalesPerson(Employee, SalesRole, CommissionPolicy):
    def __init__(self, id, name, weekly_salary, commission):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(id, name)

class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)

class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)
