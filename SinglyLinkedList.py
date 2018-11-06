# Create node
# Create Linkedlist
# Add nodes to Linkedlist
# Print Content


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        count = 0

        # Node => Data and next
        # Head => Sam => Karuna

        # Linkedlist class can be made to have an attribute object of node
        # However in the beginning ll is empty and we go on adding,removing nodes
        # Hence it is better to have a function that takes care of adding nodes than the init func
    def insertnode(self, new_node):
        # Check if ll is empty
        if self.head is None:
            self.head = new_node
        else:
            tail = self.head
            while True:
                if tail.next is None:
                    break
                else:
                    tail = tail.next
            tail.next = new_node

    def printNodes(self):
        # While traversing the list, keeping a count of nodes in nodes
        global count
        if self.head is None:
            return None
        else:
            count = 1
            tail = self.head
            while tail.next is not None:
                print tail.data
                count = count+1
                tail = tail.next
            print tail.data
            print "Total nodes in the Linkedlist: " + str(count)

    def deleteLastNode(self):
        # Using count to reach delete the last node from the penultimate node
        global count
        current = self.head
        if count == 0:
            return None
        else:
            while count > 2:
                count = count - 1
                current = current.next
            current.next = None

    def deleteFirstNode(self):
        if self.head is None:
            return None
        else:
            self.head = self.head.next

# 4 -> 6 -> 8 -> 10

    def deleteParticularNode(self, datatodelete):
        current = self.head
        previous = None
        while current.data is not None:
            if current.data == datatodelete:
                if previous is None:
                    new_head = current.next
                    current.next = None
                    return new_head
                previous.next = current.next    # This is to ensure the necessary node is deleted
                return self.head
            previous = current
            current = current.next              # This is to keep the nodes/loops moving ahead
        return self.head

    def insert(self, new_element, position):
        current = self.head
        if position == 1:
            self.head = new_element
            new_element.next = current
        else:
            while position > 1:
                current = current.next
                position = position - 1
            nextelement = current.next
            current.next = new_element
            new_element.next = nextelement

    def getposition(self, element):
        current = self.head
        count = 1
        while current.data is not element.data:
            current = current.next
            count = count+1
        print "Found node at: " + str(count)


firstNode = Node("Sam")
linkedlist = Linkedlist()
linkedlist.insertnode(firstNode)
secondNode = Node("Karuna")
linkedlist.insertnode(secondNode)
thirdNode = Node("David")
linkedlist.insertnode(thirdNode)
linkedlist.printNodes()
fourthnode = Node("Nate")
linkedlist.insertnode(fourthnode)
linkedlist.printNodes()
linkedlist.getposition(secondNode)
linkedlist.deleteParticularNode(firstNode)
# linkedlist.deleteFirstNode()
# linkedlist.deleteLastNode()
# linkedlist.printNodes()
# linkedlist.deleteParticularNode("David")
# linkedlist.printNodes()
