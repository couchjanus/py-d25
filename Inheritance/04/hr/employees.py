# базовый класс Employee, 

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

# Сначала добавили класс Manager, производный от SalaryEmployee. 
# Класс предоставляет метод work(), который будет использоваться системой производительности. 
# Метод принимает часы, которые отработал сотрудник.

class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')

# Затем мы добавили Secretary, SalesPerson и FactoryWorker, 
# а затем реализовали интерфейс work(), чтобы они могли использоваться системой производительности.

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')
class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')
class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')

# Python поддерживает множественное наследование, 
# поэтому мы решаем наследоваться как от Secretary, так и от HourlyEmployee:

# class TemporarySecretary(Secretary, HourlyEmployee):
#     pass

# Вы можете обойти MRO, изменив порядок наследования и напрямую вызвав HourlyEmployee.__init__() 
# следующим образом:

#     class TemporarySecretary(Secretary, HourlyEmployee):
#         def __init__(self, id, name, hours_worked, hour_rate):
#             HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

# Это решает проблему создания объекта, но вы столкнетесь с аналогичной проблемой 
# при попытке расчета заработной платы. Можно запустить программу, чтобы увидеть проблему:

# Теперь проблема в том, что, поскольку мы изменили порядок наследования, 
# MRO находит метод .calculate_payroll() в SalariedEmployee перед тем, как дойдет до HourlyEmployee. 
# Теперь нужно переопределить .calculate_payroll() в TemporarySecretary 
# и вызвать из него правильную реализацию:

class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)
    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)

# Метод calculate_payroll() напрямую вызывает HourlyEmployee.calculate_payroll(), 
# чтобы гарантировать, что вы получите правильный результат. 

# Теперь программа работает, потому что мы установили порядок разрешения метода, 
# явно сообщая интерпретатору, какой метод мы хотим использовать.
