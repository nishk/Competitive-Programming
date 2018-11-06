import sys


class Student:

    def __init__(self, first, last, id):
        self.first = first
        self.last = last
        self.id = id
        self.email = first + '.' + last + '@gmail.com'

    def current_instance(self):
        print self.first
        print self.last
        print self.id
        print self.email

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


stud1 = Student('Anish', 'Kirloskar', 8)
stud2 = Student('Elon', 'Musk', 64)

stud1.current_instance()
stud2.current_instance()

# print(stud1.fullname())
