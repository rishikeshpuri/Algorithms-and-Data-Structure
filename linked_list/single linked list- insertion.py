class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    # inserting node at the end
    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = newNode

    # inserting node at the Beginning
    def atBeginning(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_after_node(self, prev_node , data):
        if not prev_node:
            print('Prev node is not in the the list')
            return
        newNode = Node(data)
        newNode.next = prev_node.next
        prev_node.next = newNode


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

llist.atBeginning('A')


llist.insert_after_node(llist.head.next, 'Z')
llist.print()