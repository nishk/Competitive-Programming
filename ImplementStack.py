# Implement a Stack having following methods- push, pop, isempty, size


class Stack:
    def __init__(self):
        global top
        top = 0
        self.stack = list()

    def isempty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def Push(self, data):
        self.stack.append(data)
        return

    def Pop(self):
        if len(self.stack) == 0:
            print "Empty stack"
            return False
        else:
            self.stack.pop()

    def list_details(self):
        print len(self.stack)
        print self.stack


S1 = Stack()
S1.Push(10)
#print S1.isempty()
S1.Push(20)
S1.Push(30)
S1.Push(40)
S1.list_details()
S1.Pop()
S1.list_details()
