# productivity.py
# Класс отслеживает сотрудников в методе track(), 
# который принимает список сотрудников 
# и количество часов для отслеживания. 
class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')
