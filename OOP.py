# Employee class
# Name and details of Employee
# Salary function -> Returns annual salary based on hourly wage


class Employee:
    def __init__(self, fname, lname):
        self.first = fname
        self.last = lname
        age = 25

    @classmethod
    def emploeeproject(cls, proj):

        Current_project =
        return Current_project

    def PrintDetails(self):
        print "Employee is:" + self.first + self.last

    def CalculateAnnualSalary(self, wage):
        self.wage = wage
        salary = str(self.wage*40*52) + "$"
        print salary

    def CalculateHourlyWage(self, pay):
        self.pay = pay
        wage = pay/40/52
        print "Hourly wage is:" + str(wage) + "$"


E1 = Employee("Anish", "K")
E1.PrintDetails()
E1.CalculateAnnualSalary(10)
E1.CalculateHourlyWage(140000)
Employee.emploeeproject()
