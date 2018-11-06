class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self, side=None):
        if side is None:
            return self.length*self.breadth
        else:
            return side*side

    def cost(self, area, unit_cost=10):
        self.area = area
        self.unit_cost = unit_cost
        return self.area*self.unit_cost


side = 10
len = int(raw_input('Enter the length:'))
bre = int(raw_input('Enter the breadth:'))
rect1 = Rectangle(len, bre)
print rect1.area()
print rect1.cost(rect1.area())

##print "Area of rectangle is:",rect1.area()
