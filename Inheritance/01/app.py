# Создание иерархии классов

# Наследование — это механизм, который используется для создания иерархий связанных классов. 
# Эти связанные классы будут иметь общий интерфейс, который будет определен в базовых классах. 
# Производные классы могут специализировать интерфейс, предоставляя конкретную реализацию.

import hr.prs as hr

# Программа создает три объекта employee, по одному для каждого из производных классов. 
# Затем она создает систему начисления заработной платы и передает список сотрудников в метод .calculate_payroll(), который рассчитывает начисление заработной платы для каждого сотрудника и печатает результаты.

salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
payroll_system = hr.Payroll()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])

# базовый класс Employee не определяет метод .calculate_payroll(). 
# Это означает, что если вы создадите простой объект Employee и передадите его в Payroll, вы получите ошибку.
# employee = hr.Employee(1, 'Invalid')
