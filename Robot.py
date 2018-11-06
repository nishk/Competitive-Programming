
class Robot:

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduceself(self):
        print self.name
        print self.color
        print self.weight


r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue", 40)

r1.introduceself()
r2.introduceself()
