class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        current = Node(new_data)
        current.next = self.head
        self.head = current

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def detect_loop(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False
    #--------- OR -----------
    # Floyd’s Cycle - Finding Algorithm:
    def detectLoop(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("Loop Found")
            else:
                print("No LOOP")
                return



llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.print_list()

# Create a loop for testing
llist.head.next.next.next.next = llist.head

if llist.detect_loop():
    print('Loop found')
else:
    print('No loop')

print()
llist.detectLoop()