class Operations:
    def __init__(self):
        pass

    def factorial(self, number):
        self.number = number
        flag = self.number
        if number is 0:
            return 1
        else:
            while flag > 0:
                self.number = self.number*flag
                flag = flag - 1
            return self.number


num = input("Input number to calculate factorial")
o1 = Operations()
print "Factorial is " + o1.factorial()
