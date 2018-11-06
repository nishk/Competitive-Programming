class Student():
    no_of_students = 0
    annual_raise = 1.02

    def __init__(self, first, last, wage):
        self.first = first
        self.last = last
        self.wage = wage
        Student.no_of_students += 1

    def student_email(self):
        print self.first + '.' + self.last + '@company.com'

    def student_fullname(self):
        print '{} {}'.format(self.first, self.last)

    def apply_raise(self, annual_raise=None):
        if annual_raise is None:
            self.wage = self.wage*Student.annual_raise
        else:
            self.wage = self.wage*annual_raise
        return self.wage


class Teaching_Assistant(Student):
    annual_raise = 1.05

    def __init__(self, first, last, wage, subject):
        #super().__init__(first, last, wage)
        Student.__init__(self, first, last, wage)
        self.subject = subject


class Professor(Student):

    def __init__(self, first, last, wage, studs=None):
        Student.__init__(self, first, last, wage)
        if studs is None:
            self.studs = []
        else:
            self.studs = studs

    def add_student(self, stu):
        if stu not in self.studs:
            self.studs.append(stu)

    def rem_student(self, stu):
        if stu in self.studs:
            self.studs.remove(stu)

    def print_students(self):
        for stu in self.studs:
            stu.student_fullname()


stud1 = Teaching_Assistant('Anish', 'Kirloskar', 10, 'Economics')
stud2 = Teaching_Assistant('Houman', 'Homayoun', 15, 'CompArch')
# stud1.student_email()
#print stud1.subject

prof1 = Professor('Tom', 'Storey', 90000, [stud1, stud2])
prof1.student_fullname()
prof1.student_email()
prof1.print_students()


#print stud1.student_email()
# stud1.student_fullname()
#print stud1.wage
#print stud1.apply_raise(1.04)
