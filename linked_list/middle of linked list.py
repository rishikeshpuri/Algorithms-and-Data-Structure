class Node:

    # Function to initialise the node object
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

    # at starting
    def at_begining_insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_middle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head:
            while fast_ptr and fast_ptr.next:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            print("the middle element is: ", slow_ptr.data)

list1 = LinkedList()
list1.at_begining_insert(5)
list1.at_begining_insert(4)
list1.at_begining_insert(2)
list1.at_begining_insert(3)
list1.at_begining_insert(1)
list1.print()
list1.print_middle()