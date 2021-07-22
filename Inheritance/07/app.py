from hr.prs import Payroll
import hr.employees
from hr.productivity import ProductivitySystem
import hr.contacts
from hr.employees import EmployeeDatabase
    
# Используем композицию для создания лучшего дизайна, 

# Начнем с реализации системы ProductivitySystem:
#     # productivity.py
#     class ProductivitySystem:
#         def __init__(self):
#             self._roles = {
#                 'manager': ManagerRole,
#                 'secretary': SecretaryRole,
#                 'sales': SalesRole,
#                 'factory': FactoryRole,
#             }
#         def get_role(self, role_id):
#             role_type = self._roles.get(role_id)
#             if not role_type:
#                 raise ValueError('role_id')
#             return role_type()
#         def track(self, employees, hours):
#             print('Tracking Employee Productivity')
#             print('==============================')
#             for employee in employees:
#                 employee.work(hours)
#             print('')

# Класс ProductivitySystem определяет некоторые роли, используя строковый идентификатор, сопоставленный с классом роли, который реализует роль. 
# Он предоставляет метод .get_role(), который при наличии идентификатора роли возвращает объект типа роли. 
# Если роль не найдена, возникает исключение ValueError.

# Он также реализует предыдущую функциональность в методе .track(), где, учитывая список сотрудников, отслеживается производительность этих сотрудников.

# Теперь реализуем различные классы ролей:
#     # productivity.py
#     class ManagerRole:
#         def perform_duties(self, hours):
#             return f'screams and yells for {hours} hours.'
#     class SecretaryRole:
#         def perform_duties(self, hours):
#             return f'does paperwork for {hours} hours.'
#     class SalesRole:
#         def perform_duties(self, hours):
#             return f'expends {hours} hours on the phone.'
#     class FactoryRole:
#         def perform_duties(self, hours):
#             return f'manufactures gadgets for {hours} hours.'

# Каждая из реализованных вами ролей предоставляет функцию .perform_duties(), которая принимает количество отработанных часов. Методы возвращают строку, представляющую обязанности.

# Классы ролей не зависят друг от друга, но они предоставляют один и тот же интерфейс, поэтому они взаимозаменяемы. Позже вы увидите, как они используются в приложении.

# Теперь можно реализовать Payroll для приложения:
#     class PayrollSystem:
#         def __init__(self):
#             self._employee_policies = {
#                 1: SalaryPolicy(3000),
#                 2: SalaryPolicy(1500),
#                 3: CommissionPolicy(1000, 100),
#                 4: HourlyPolicy(15),
#                 5: HourlyPolicy(9)
#             }
#         def get_policy(self, employee_id):
#             policy = self._employee_policies.get(employee_id)
#             if not policy:
#                 return ValueError(employee_id)
#             return policy
#         def calculate_payroll(self, employees):
#             print('Calculating Payroll')
#             print('===================')
#             for employee in employees:
#                 print(f'Payroll for: {employee.id} - {employee.name}')
#                 print(f'- Check amount: {employee.calculate_payroll()}')
#                 if employee.address:
#                     print('- Sent to:')
#                     print(employee.address)
#                 print('')

# Система Payroll ведет внутреннюю базу данных политик расчета заработной платы для каждого сотрудника. 
# Она предоставляет функцию .get_policy(), которая, учитывая идентификатор сотрудника, возвращает свою политику расчета заработной платы. 
# Если указанный идентификатор не существует в системе, метод вызывает исключение ValueError.

# Теперь можно реализовать классы политики заработной платы:
#     class PayrollPolicy:
#         def __init__(self):
#             self.hours_worked = 0
#         def track_work(self, hours):
#             self.hours_worked += hours
#     class SalaryPolicy(PayrollPolicy):
#         def __init__(self, weekly_salary):
#             super().__init__()
#             self.weekly_salary = weekly_salary
#         def calculate_payroll(self):
#             return self.weekly_salary
#     class HourlyPolicy(PayrollPolicy):
#         def __init__(self, hour_rate):
#             super().__init__()
#             self.hour_rate = hour_rate
#         def calculate_payroll(self):
#             return self.hours_worked * self.hour_rate
#     class CommissionPolicy(SalaryPolicy):
#         def __init__(self, weekly_salary, commission_per_sale):
#             super().__init__(weekly_salary)
#             self.commission_per_sale = commission_per_sale
#         @property
#         def commission(self):
#             sales = self.hours_worked / 5
#             return sales * self.commission_per_sale
#         def calculate_payroll(self):
#             fixed = super().calculate_payroll()
#             return fixed + self.commission

# Сначала реализуется класс PayrollPolicy, который служит базовым классом для всех политик расчета заработной платы. Этот класс отслеживает часы работы hours_worked, которые являются общими для всех политик расчета заработной платы.

# Другие классы политик являются производными от PayrollPolicy. Мы используем наследование здесь, потому что мы хотим использовать реализацию PayrollPolicy. Кроме того, SalaryPolicy, HourlyPolicy и CommissionPolicy являются PayrollPolicy.

# SalaryPolicy инициализируется значением weekly_salary, которое затем используется в .calculate_payroll(). 
# HourlyPolicy инициализируется с помощью hour_rate и реализует .calculate_payroll(), используя базовый класс hours_worked.

# Класс CommissionPolicy является производным от SalaryPolicy, потому что он хочет наследовать свою реализацию. Он инициализируется с параметрами weekly_salary, но для него также требуется параметр commission_per_sale.

# commission_per_sale используется для вычисления .commission, которое реализовано как свойство, поэтому она вычисляется по запросу. 
# предполагаем, что продажа происходит каждые 5 часов работы, а .commission – это количество продаж, умноженное на значение commission_per_sale.

# CommissionPolicy реализует метод .calculate_payroll(), сначала используя реализацию в SalaryPolicy, а затем добавляя рассчитанную комиссию.

# Теперь вы можете добавить класс AddressBook для управления адресами сотрудников:
#     # contacts.py
#     class AddressBook:
#         def __init__(self):
#             self._employee_addresses = {
#                 1: Address('121 Admin Rd.', 'Concord', 'NH', '03301'),
#                 2: Address('67 Paperwork Ave', 'Manchester', 'NH', '03101'),
#                 3: Address('15 Rose St', 'Concord', 'NH', '03301', 'Apt. B-1'),
#                 4: Address('39 Sole St.', 'Concord', 'NH', '03301'),
#                 5: Address('99 Mountain Rd.', 'Concord', 'NH', '03301'),
#             }
#         def get_employee_address(self, employee_id):
#             address = self._employee_addresses.get(employee_id)
#             if not address:
#                 raise ValueError(employee_id)
#             return address

# Класс AddressBook хранит внутреннюю базу данных объектов Address для каждого сотрудника. Он предоставляет метод get_employee_address(), который возвращает адрес указанного идентификатора сотрудника. Если идентификатор сотрудника не существует, то возникает ошибка ValueError.

# Реализация класса Address остается такой же, как и раньше:
#     # contacts.py
#     class Address:
#         def __init__(self, street, city, state, zipcode, street2=''):
#             self.street = street
#             self.street2 = street2
#             self.city = city
#             self.state = state
#             self.zipcode = zipcode
#         def __str__(self):
#             lines = [self.street]
#             if self.street2:
#                 lines.append(self.street2)
#             lines.append(f'{self.city}, {self.state} {self.zipcode}')
#             return '\n'.join(lines)

# Класс управляет компонентами адреса и обеспечивает красивое представление адреса.

# Далее реализуем класс EmployeeDatabase:
#     # employees.py
#     from productivity import ProductivitySystem
#     from hr import PayrollSystem
#     from contacts import AddressBook
#     class EmployeeDatabase:
#         def __init__(self):
#             self._employees = [
#                 {
#                     'id': 1,
#                     'name': 'Mary Poppins',
#                     'role': 'manager'
#                 },
#                 {
#                     'id': 2,
#                     'name': 'John Smith',
#                     'role': 'secretary'
#                 },
#                 {
#                     'id': 3,
#                     'name': 'Kevin Bacon',
#                     'role': 'sales'
#                 },
#                 {
#                     'id': 4,
#                     'name': 'Jane Doe',
#                     'role': 'factory'
#                 },
#                 {
#                     'id': 5,
#                     'name': 'Robin Williams',
#                     'role': 'secretary'
#                 },
#             ]
#             self.productivity = ProductivitySystem()
#             self.payroll = PayrollSystem()
#             self.employee_addresses = AddressBook()
#         @property
#         def employees(self):
#             return [self._create_employee(**data) for data in self._employees]
#         def _create_employee(self, id, name, role):
#             address = self.employee_addresses.get_employee_address(id)
#             employee_role = self.productivity.get_role(role)
#             payroll_policy = self.payroll.get_policy(id)
#             return Employee(id, name, address, employee_role, payroll_policy)

# EmployeeDatabase отслеживает всех сотрудников компании. Для каждого сотрудника он отслеживает id, name и role. У него есть экземпляр ProductivitySystem, PayrollSystem и AddressBook. Эти экземпляры используются для создания сотрудников.

# Он содержит свойство .employees, которое возвращает список сотрудников. Объекты Employee создаются во внутреннем методе ._create_employee(). Обратите внимание, что у нас нет разных типов классов Employee. Нам просто нужно реализовать один класс Employee:

#     In employees.py
#     class Employee:
#         def __init__(self, id, name, address, role, payroll):
#             self.id = id
#             self.name = name
#             self.address = address
#             self.role = role
#             self.payroll = payroll
#         def work(self, hours):
#             duties = self.role.perform_duties(hours)
#             print(f'Employee {self.id} - {self.name}:')
#             print(f'- {duties}')
#             print('')
#             self.payroll.track_work(hours)
#         def calculate_payroll(self):
#             return self.payroll.calculate_payroll()

# Класс Employee инициализируется атрибутами id, name и address. Он также требует роли производительности для работника role и политики оплаты труда payroll.

# Класс предоставляет метод .work(), который принимает отработанные часы. Этот метод сначала извлекает обязанности duties из роли role. Другими словами, он делегирует объекту role выполнения своих обязанностей.
# Таким же образом он делегирует объекту payroll отслеживания рабочего времени hours. Заработная плата payroll использует эти часы для расчета заработной платы.
  
productivity_system = ProductivitySystem()
payroll_system = Payroll()
employee_database = EmployeeDatabase()
employees = employee_database.employees
productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)
