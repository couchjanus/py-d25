# productivity.py
# все, что связано с производительностью, должно быть вместе в одном модуле, 

class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name}: {result}')
        print('')

class ManagerRole:
    def work(self, hours):
        return f'screams and yells for {hours} hours.'
class SecretaryRole:
    def work(self, hours):
        return f'expends {hours} hours doing office paperwork.'
class SalesRole:
    def work(self, hours):
        return f'expends {hours} hours on the phone.'
class FactoryRole:
    def work(self, hours):
        return f'manufactures gadgets for {hours} hours.'

# Модуль производительности реализует класс ProductivitySystem, а также связанные с ним роли. Классы реализуют интерфейс work(), требуемый системой, но они не получены от Employee.
