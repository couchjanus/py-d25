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


# Производные классы Employee используются в двух разных системах:
#     Система производительности, которая отслеживает производительность сотрудников.
#     Система начисления заработной платы, которая рассчитывает заработную плату сотрудника.

# Это означает, что все, что связано с производительностью, должно быть вместе в одном модуле, 
# а все, что связано с заработной платой, должно быть вместе в другом. 

# модуль производительности: In productivity.py
# Модуль производительности реализует класс ProductivitySystem, а также связанные с ним роли. Классы реализуют интерфейс work(), требуемый системой, но они не получены от Employee.


# class Payroll:
# Модуль prs реализует систему Payroll, которая рассчитывает заработную плату для сотрудников. Он также реализует классы политики для расчета заработной платы. 
# Классы политики больше не являются производными от Employee.


# Теперь добавим необходимые классы в модуль employees.py
# Модуль employees импортирует политики и роли из других модулей и реализует различные типы Employee. 
# Мы все еще используем множественное наследование для наследования реализации классов политики заработной платы и ролей производительности, но реализация каждого класса должна иметь дело только с инициализацией.
