# Система управления персоналом должна обрабатывать платежную ведомость для сотрудников компании
# существуют разные типы работников в зависимости от того, как рассчитывается их заработная плата.

# реализация класса Payroll, который будет обрабатывает платежную ведомость:

# Payroll реализует метод .calculate_payroll(), 
# который принимает коллекцию сотрудников и печатает их идентификатор, имя и
# сумму чека, используя метод .calculate_payroll(), для каждого объекта сотрудника.

class Payroll:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')

# реализуем базовый класс Employee, 
# который обрабатывает общий интерфейс для каждого типа сотрудника:

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Employee является базовым классом для всех типов сотрудников. 
# Он объявлен с id и name.

# Система управления персоналом требует, чтобы каждый обработанный Employee
# имел интерфейс .calculate_payroll(), 
# который возвращает еженедельную зарплату сотруднику. 
# Реализация этого интерфейса отличается в зависимости от типа Employee.

# административные работники имеют фиксированную зарплату, 
# поэтому каждую неделю им платят одну и ту же сумму:

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary

# производный класс SalaryEmployee, который наследует Employee. 
# Класс инициализируется с помощью id и name базовым классом, 
# для этого мы используете super() для инициализации членов базового класса.

# SalaryEmployee также требует параметр инициализации weekly_salary, 
# сумму, которую сотрудник зарабатывает за неделю.

# Класс содержит обязательный метод .calculate_payroll(), 
# Его реализация просто возвращает сумму, хранящуюся в weekly_salary.

# В компании также работают рабочие, которые получают почасовую оплату, 
# добавим HourlyEmployee:

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

# Класс HourlyEmployee инициализируется с помощью id и name, переменных базового класса, 
# hours_worked и hour_rate, необходимые для расчета заработной платы. 
# Метод .calculate_payroll() реализован путем возврата отработанных часов, умноженных на часовую ставку.

# в компании работают торговые партнеры, 
# которым выплачивается фиксированная зарплата плюс комиссия, 
# основанная на их продажах 

# создадим класс CommissionEmployee:

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

# CommissionEmployee является производным от SalaryEmployee, потому что оба класса имеют weekly_salary. 
# CommissionEmployee инициализируется значением commission, основанным на продажах для сотрудника.

# .calculate_payroll() использует реализацию базового класса для получения фиксированной зарплаты fixed и добавляет значение комиссии.

# у CommissionEmployee есть доступ к свойству weekly_salary напрямую, и мы могли бы реализовать .calculate_payroll(), используя значение этого свойства.

# Проблема с прямым доступом к свойству заключается в том, что если изменяется реализация SalaryEmployee.calculate_payroll(), нам также придется изменить реализацию CommissionEmployee.calculate_payroll(). 
# Лучше полагаться на реализованный метод в базовом классе и расширять функциональность по мере необходимости.
