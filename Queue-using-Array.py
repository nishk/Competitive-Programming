class QueueArray:
    def __init__(self, maxsize):
        self.top = 0
        self.maxsize = maxsize
        self.Queue = list()

    def isempty(self):
        if len(self.Queue) == 0:
            return True
        else:
            return False

    def Push(self, data):
        if self.top < self.maxsize:
            self.Queue.append(data)
            self.top += 1
        else:
            print "Queue is full"

    def Pop(self):
        if (len(self.Queue)) == 0:
            print "Queue empty - nothing to pop :("
        else:
            element = self.Queue[0]
            self.Queue.remove(element)

    def Queue_details(self):
        print "length of Queue: " + str(len(self.Queue))
        print self.Queue
        print "Space available for: " + str(self.maxsize-self.top)


S1 = QueueArray(3)
print S1.isempty()
S1.Push(5)
#print S1.isempty()
S1.Push(10)
S1.Push(15)
print S1.Queue_details()
# S1.Push(20)
#print S1.Queue_details()
S1.Pop()
print S1.Queue_details()
