import hr.prs
import hr.employees
import hr.productivity
import hr.contacts

# Композиция – это объектно-ориентированная концепция дизайна, которая моделирует отношения. В композиции класс, известный как составной, содержит объект другого класса, известный как компонент. Другими словами, составной класс имеет компонент другого класса.

# Композиция позволяет составным классам повторно использовать реализацию компонентов, которые она содержит. Составной класс не наследует интерфейс класса компонента, но может использовать его реализацию.

# Композиционные отношения между двумя классами считаются слабосвязанными. Это означает, что изменения в классе компонентов редко влияют на составной класс, а изменения в составном классе никогда не влияют на класс компонентов.

# Это обеспечивает лучшую адаптируемость к изменениям и позволяет приложениям вводить новые требования, не затрагивая существующий код.

# При рассмотрении двух конкурирующих программных проектов, один из которых основан на наследовании, а другой – на композиции, решение для композиции обычно является наиболее гибким. Теперь посмотрим, как работает композиция.

# Мы уже использовали композицию в наших примерах. Если вы посмотрите на класс Employee, вы увидите, что он содержит два атрибута:
#     id для идентификации сотрудника.
#     name, содержащее имя сотрудника.

# Эти два атрибута являются объектами, которые есть у класса Employee. 
# Другим атрибутом для Employee может быть Address:
#     contacts.py
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

# Мы реализовали базовый класс адресов, который содержит обычные компоненты для адреса. 
# Сделали атрибут street2 необязательным, поскольку не все адреса будут иметь этот компонент.
# Реализовали __str__(), чтобы обеспечить красивое представление Address. Можно увидеть эту реализацию в интерактивном интерпритаторе:

from hr.contacts import Address
address = Address('55 Main St.', 'Concord', 'NH', '03301')
print(address)

# Когда вы выводите на экран переменную address, вызывается специальный метод __str__(). Поскольку мы перегрузили метод, чтобы вернуть строку, отформатированную как адрес, мы получили хорошее, читаемое представление. 

# Теперь можно добавить Address в класс Employee с помощью композиции:
#     employees.py
#     class Employee:
#         def __init__(self, id, name):
#             self.id = id
#             self.name = name
#             self.address = None

# Мы инициализируем атрибут address значением None на данный момент, чтобы сделать его необязательным, но, сделав это, теперь можно назначить Address для Employee. 

# Композиция – это слабо связанные отношения, которые часто не требуют, чтобы составной класс обладал знаниями о компоненте.

# Теперь можно изменить класс Payroll, чтобы использовать атрибут address в Employee:

#     class PayrollSystem:
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

# Здесь мы проверяем, есть ли у объекта employee адрес, и если он есть, печатаем его. 
# Теперь можно изменить программу, чтобы назначить некоторые адреса сотрудникам:

manager = hr.employees.Manager(1, 'Mary Poppins', 3000)
manager.address = hr.contacts.Address(
        '121 Admin Rd', 
        'Concord', 
        'NH', 
        '03301'
)
secretary = hr.employees.Secretary(2, 'John Smith', 1500)
secretary.address = hr.contacts.Address(
        '67 Paperwork Ave.', 
        'Manchester', 
        'NH', 
        '03101'
)
sales_guy = hr.employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = hr.employees.FactoryWorker(4, 'Jane Doe', 40, 15)
temporary_secretary = hr.employees.TemporarySecretary(5, 'Robin Williams', 40, 9)
company_employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]
productivity_system = hr.productivity.ProductivitySystem()
productivity_system.track(company_employees, 40)
payroll_system = hr.prs.Payroll()
payroll_system.calculate_payroll(company_employees)

# Мы добавили пару адресов к объектам manager и secretary. 

# Класс Employee использует реализацию класса Address без знания того, что такое объект Address или как он представлен. Этот тип дизайна настолько гибок, что можно изменить класс Address без какого-либо влияния на класс Employee.

# Композиция более гибкая, чем наследование, потому что она моделирует слабо связанные отношения. Изменения в классе компонентов оказывают минимальное влияние или вообще не влияют на составной класс. Дизайн, основанный на композиции, более подходит для изменений.

# Можно изменять поведение, добавляя новые компоненты, которые реализуют это поведение, вместо добавления новых классов в вашу иерархию.

# Самая большая проблема заключается не столько в количестве классов в дизайне, сколько в том, насколько тесно связаны отношения между этими классами. Сильно связанные классы влияют друг на друга при внесении изменений.
