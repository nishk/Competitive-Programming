class StackArray:
    def __init__(self, maxsize):
        self.top = 0
        self.maxsize = maxsize
        self.stack = list()

    def isempty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def Push(self, data):
        if self.top < self.maxsize:
            self.stack.append(data)
            self.top += 1
        else:
            print "Stack is full"

    def Pop(self):
        if (len(self.stack)) == 0:
            print "Stack empty - nothing to pop :("
        else:
            self.stack.pop()
            self.top -= 1

    def Stack_details(self):
        print "length of stack: " + str(len(self.stack))
        print self.stack
        print "Space available for: " + str(self.maxsize-self.top)


S1 = StackArray(3)
print S1.isempty()
S1.Push(5)
#print S1.isempty()
S1.Push(10)
S1.Push(15)
print S1.Stack_details()
# S1.Push(20)
#print S1.Stack_details()
S1.Pop()
print S1.Stack_details()
