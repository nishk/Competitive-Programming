# Implement a Queue having following methods- push, pop, isempty, size


class Queue:
    def __init__(self):
        global top
        top = 0
        self.Queue = list()

    def isempty(self):
        if len(self.Queue) == 0:
            return True
        else:
            return False

    def Push(self, data):
        self.Queue.append(data)
        return

    def Pop(self):
        if len(self.Queue) == 0:
            print "Empty Queue"
            return False
        else:
            x = self.Queue[0]
            self.Queue.remove(x)

    def list_details(self):
        print self.Queue


S1 = Queue()
S1.Push(10)
#print S1.isempty()
S1.Push(20)
S1.Push(30)
S1.Push(40)
S1.list_details()
S1.Pop()
S1.list_details()
