import hr.prs
import hr.employees
import hr.productivity

# Мы удалили импорт модуля abc, поскольку класс Employee не обязательно должен быть абстрактным. 
# Мы также удалили из него абстрактный метод calculate_payroll(), 
# поскольку он не обеспечивает никакой реализации.

# Поскольку .calculate_payroll() – это просто интерфейс к методу Payroll.calculate_payroll(), 
# нам не нужно реализовывать его в базовом классе Employee.

# CommissionEmployee наследует реализацию и интерфейс SalaryEmployee. 
# метод CommissionEmployee.calculate_payroll() 
# использует реализацию базового класса, поскольку для реализации своей собственной версии 
# он использует результат из super().calculate_payroll().

# Проблема взрыва класса

# наследование может привести к огромной иерархической структуре классов, 
# которую трудно понять и поддерживать. 
# Эта ситуация известна как проблема взрыва класса (class explosion problem).

# ProductivitySystem отслеживает производительность на основе ролей сотрудников. 
# Нам потребуются несколько ролей сотрудников:
#     Менеджеры
#     Секретари
#     Продавцы
#     Фабричные рабочие

manager = hr.employees.Manager(1, 'Mary Poppins', 3000)
secretary = hr.employees.Secretary(2, 'John Smith', 1500)
sales_guy = hr.employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = hr.employees.FactoryWorker(2, 'Jane Doe', 40, 15)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
]
productivity_system = hr.productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = hr.prs.Payroll()
payroll_system.calculate_payroll(employees)

# Программа создает список сотрудников разных типов. 
# Список сотрудников отправляется в систему производительности для отслеживания их работы в течение 40 часов. 
# Затем тот же список сотрудников отправляется в систему расчета заработной платы.

# Программа показывает сотрудников, работающих в течение 40 часов через систему производительности. 
# Затем она рассчитывает и отображает платежную ведомость для каждого из сотрудников.

# мы должны были добавить четыре новых класса 
# для поддержки изменений. По мере появления новых требований наша иерархия классов неизбежно будет расти, 
# что приведет к проблеме взрыва классов, когда наши иерархии станут настолько большими, 
# что их будет трудно понять и поддерживать.