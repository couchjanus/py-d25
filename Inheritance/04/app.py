# Наследование нескольких классов
# Python – один из немногих современных языков программирования, который поддерживает множественное наследование. Множественное наследование – это возможность получить класс из нескольких базовых классов одновременно.

# Множественное наследование имеет плохую репутацию, более того большинство современных языков программирования не поддерживают его. Вместо этого современные языки программирования поддерживают концепцию интерфейсов. В этих языках вы наследуете от одного базового класса, а затем реализуете несколько интерфейсов, поэтому ваш класс можно повторно использовать в различных ситуациях.

# Этот подход накладывает некоторые ограничения на ваши проекты. Вы можете унаследовать реализацию только одного класса. Вы можете реализовать несколько интерфейсов, но вы не можете наследовать реализацию нескольких классов.

# Это ограничение хорошо для разработки программного обеспечения, потому что оно заставляет вас создавать свои классы с меньшим количеством зависимостей друг от друга. 

# Допустим что, иногда нанимают временных секретарей, когда слишком много бумажной работы. Класс TemporarySecretary выполняет роль секретаря в контексте ProductivitySystem, но для целей расчета заработной платы используем HourlyEmployee.

# Если посмотреть на иерархию классов. Все немного усложнилось, но вы все еще можете понять, как это работает. Кажется, у вас есть два варианта:
#1. Создать на основе Secretary: Можно наследоваться от Secretary, чтобы наследовать метод .work() для роли, а затем переопределить метод .calculate_payroll(), чтобы реализовать его как HourlyEmployee.
#2. Создать на основе HourlyEmployee: Можно наследоваться от HourlyEmployee для наследования метода .calculate_payroll(), а затем переопределить метод .work() для реализации его в качестве Secretary.

# Python поддерживает множественное наследование, поэтому мы решаем наследоваться как от Secretary, так и от HourlyEmployee:
#     # In employees.py
#     class TemporarySecretary(Secretary, HourlyEmployee):
#         pass

# Python позволяет нам наследоваться от двух разных классов, указав их в скобках в объявлении класса.

# добавим нового временного сотрудника секретаря:

import hr.prs
import hr.employees
import hr.productivity


manager = hr.employees.Manager(1, 'Mary Poppins', 3000)
secretary = hr.employees.Secretary(2, 'John Smith', 1500)
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

# Запустим программу для проверки:
#     $ python program.py
#     Traceback (most recent call last):
#      File ".\program.py", line 9, in <module>
#       temporary_secretary = employee.TemporarySecretary(5, 'Robin Williams', 40, 9)
#     TypeError: __init__() takes 4 positional arguments but 5 were given

# Мы получим исключение TypeError, говорящее о том, что 4 позиционных аргумента были ожидаемыми, но только 5 были заданы.

# Это потому, что вы наследовали TemporarySecretary сначала от Secretary, а затем от HourlyEmployee, поэтому интерпретатор пытается использовать Secretary.__init__() для инициализации объекта.

# изменим это:
#     class TemporarySecretary(HourlyEmployee, Secretary):
#         pass

# Теперь если снова запустить программу мы получим следующее:
#     $ python program.py
#     Traceback (most recent call last):
#      File ".\program.py", line 9, in <module>
#       temporary_secretary = employee.TemporarySecretary(5, 'Robin Williams', 40, 9)
#      File "employee.py", line 16, in __init__
#       super().__init__(id, name)
#     TypeError: __init__() missing 1 required positional argument: 'weekly_salary'

# Теперь кажется, что нам не хватает параметра weekly_salary, который необходим для инициализации Secretary, но этот параметр не имеет смысла в контексте TemporarySecretary, потому что это HourlyEmployee.

# Может быть, реализация TemporarySecretary.__init__() поможет:
#     # In employees.py
#     class TemporarySecretary(HourlyEmployee, Secretary):
#         def __init__(self, id, name, hours_worked, hour_rate):
#             super().__init__(id, name, hours_worked, hour_rate)

# Попробуем:
#     $ python program.py
#     Traceback (most recent call last):
#      File ".\program.py", line 9, in <module>
#       temporary_secretary = employee.TemporarySecretary(5, 'Robin Williams', 40, 9)
#      File "employee.py", line 54, in __init__
#       super().__init__(id, name, hours_worked, hour_rate)
#      File "employee.py", line 16, in __init__
#       super().__init__(id, name)
#     TypeError: __init__() missing 1 required positional argument: 'weekly_salary'

# Это тоже не сработало. Хорошо, пришло время погрузиться в порядок разрешения методов Python (MRO – method resolution order), чтобы понять, что происходит.

# При обращении к методу или атрибуту класса Python использует MRO, чтобы найти его. MRO также используется super() для определения, какой метод или атрибут вызывать.

# Вы можете посмотреть как работает MRO класса TemporarySecretary с помощью интерактивного интерпритатора:

#     >>> from employees import TemporarySecretary
#     >>> TemporarySecretary.__mro__
#     (<class 'employees.TemporarySecretary'>,
#      <class 'employees.HourlyEmployee'>,
#      <class 'employees.Secretary'>,
#      <class 'employees.SalaryEmployee'>,
#      <class 'employees.Employee'>,
#      <class 'object'>
#     )

# MRO показывает порядок, в котором Python будет искать соответствующий атрибут или метод. В нашем примере когда мы создаем объект TemporarySecretary происходит следующее:
#     Вызывается метод TemporarySecretary.__init__(self, id, name, hours_worked, hour_rate).
#     Вызов super().__init__(id, name, hours_worked, hour_rate) соответствует HourlyEmployee.__init__(self, id, name, hour_worked, hour_rate)
#     HourlyEmployee вызывает super().__init__(id, name), который MRO собирается сопоставить с Secretary.__init__(), который унаследован от SalaryEmployee.__init__(self, id, name, weekly_salary)

# Поскольку параметры не совпадают, возникает исключение TypeError.
# Вы можете обойти MRO, изменив порядок наследования и напрямую вызвав HourlyEmployee.__init__() следующим образом:
#     class TemporarySecretary(Secretary, HourlyEmployee):
#         def __init__(self, id, name, hours_worked, hour_rate):
#             HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

# Это решает проблему создания объекта, но вы столкнетесь с аналогичной проблемой при попытке расчета заработной платы. Можно запустить программу, чтобы увидеть проблему:

# Теперь проблема в том, что, поскольку мы изменили порядок наследования, MRO находит метод .calculate_payroll() в SalariedEmployee перед тем, как дойдет до HourlyEmployee. Теперь нужно переопределить .calculate_payroll() в TemporarySecretary и вызвать из него правильную реализацию:

#     class TemporarySecretary(Secretary, HourlyEmployee):
#         def __init__(self, id, name, hours_worked, hour_rate):
#             HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)
#         def calculate_payroll(self):
#             return HourlyEmployee.calculate_payroll(self)

# Метод calculate_payroll() напрямую вызывает HourlyEmployee.calculate_payroll(), чтобы гарантировать, что вы получите правильный результат. Вы можете снова запустить программу, чтобы увидеть, как теперь она будет работает:

# Теперь программа работает, потому что мы установили порядок разрешения метода, явно сообщая интерпретатору, какой метод мы хотим использовать.

# множественное наследование может сбивать с толку, особенно когда вы сталкиваетесь с проблемой алмаза (diamond).

# TemporarySecretary использует множественное наследование для наследования от двух классов, которые в конечном итоге также наследуются от Employee. Это приводит к двум путям достижения базового класса Employee, чего нужно обязательно избегать в своих проектах.

# Проблема алмазов возникает, когда используется множественное наследование и наследование от двух классов, имеющих общий базовый класс. Это может вызвать неправильную версию метода для вызова.

# Python предоставляет способ принудительного вызова правильного метода, и анализ MRO может помочь понять проблему.

# Тем не менее, когда вы сталкиваетесь с проблемой алмазов, лучше переосмыслить дизайн.
