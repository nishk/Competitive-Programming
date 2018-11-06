class Employee:
    no_of_employees = 0
    annual_raise = 1.02

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.fullname = self.first+self.last
        self.salary = salary

    def employee_details(self):
        print '{} {}'.format(self.first, self.last)

    def employee_email_id(self):
        return self.fullname + '@company.com'

    def salary_raise(self, annual_raise=None):
        if annual_raise is None:
            self.salary = self.salary*Employee.annual_raise
        else:
            self.salary = self.salary*annual_raise
        return self.salary


class Manager(Employee):
    annual_raise = 1.04

    def __init__(self, first, last, salary, employees=None):
        Employee.__init__(self, first, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            emp.employee_details()
            # emp.employee_email_id()


emp_1 = Employee('Cody', 'Schafer', 100000)
emp_2 = Employee('Marques', 'Brownlee', 180000)
mgr_1 = Manager('Saurabh', 'Lohokare', 200000, [emp_1, emp_2])

# print mgr_1.employee_details()
print mgr_1.employee_email_id()
print mgr_1.print_employees()

# print emp_1.employee_details()
# print emp_1.employee_email_id()
# print emp_1.salary_raise()
# print emp_1.salary_raise(1.1)
# emp_1.employee_details()
