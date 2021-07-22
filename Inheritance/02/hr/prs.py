from abc import ABC, abstractmethod

# Абстрактные базовые классы в Python
# Класс Employee называется абстрактным базовым классом. 
# Абстрактные базовые классы существуют для наследования, 
# но никогда сами не используются для создания объектов. 
# Python предоставляет модуль abc для определения абстрактных базовых классов.

# Вы можете использовать подчеркивания в имени класса, чтобы сообщить, 
# что объекты этого класса не должны создаваться. 
# Подчеркивания обеспечивают дружественный способ предотвращения неправильного использования кода,
# но они не мешают пользователям создавать экземпляры этого класса.

# Модуль abc в стандартной библиотеке Python предоставляет функциональные возможности 
# для предотвращения создания объектов из абстрактных базовых классов.

# изменим реализацию класса Employee, чтобы гарантировать, 
# что он не может быть использован для создания объекта:

# Мы наследуем Employee от ABC, делая его абстрактным базовым классом. 
# объекты типа Employee не могут быть созданы.

# class Payroll
class Payroll:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')

class Employee(ABC):
    
    # Employee является базовым классом для всех типов сотрудников. 
    # Он объявлен с id и name.

    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    # Система управления персоналом требует, чтобы каждый обработанный Employee
    # имел интерфейс .calculate_payroll(), 
    # который возвращает еженедельную зарплату сотруднику. 
    # Реализация этого интерфейса отличается в зависимости от типа Employee.

    # декорируем метод .calculate_payroll() 
    # с помощью декоратора @abstractmethod.
    
    
    @abstractmethod
    def calculate_payroll(self):
        pass
    
    # При условии, если классы являются производными от Employee, 
    # они должны переопределить абстрактный метод .calculate_payroll(). 

# производный класс SalaryEmployee, который наследует Employee. 
# административные работники имеют фиксированную зарплату, 
# поэтому каждую неделю им платят одну и ту же сумму:
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary

# Класс инициализируется с помощью id и name базовым классом, 
# для этого мы используете super() для инициализации членов базового класса.

# SalaryEmployee также требует параметр инициализации weekly_salary, 
# сумму, которую сотрудник зарабатывает за неделю.

# Класс содержит обязательный метод .calculate_payroll(), 
# Его реализация просто возвращает сумму, хранящуюся в weekly_salary.

# class HourlyEmployee:
# рабочие, которые получают почасовую оплату, 
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


# класс CommissionEmployee:
# торговые партнеры, которым выплачивается фиксированная зарплата плюс комиссия, основанная на их продажах 
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
