class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_dllist(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.prev = None

        current_node = self.head
        while current_node.next:

            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.prev = None
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = Node

    def add_after_node(self, key, data):
        current_node = self.head
        new_node = Node(data)
        while current_node:
            if current_node.next is None and current_node.data == key:
                # ---------------------------------
                # if current_node is None:
                #     current_node = new_node
                #     new_node.prev = None
                # while current_node:
                #     current_node = current_node.next
                # current_node.next = new_node
                # new_node.prev = current_node
                # new_node.next = Node
                # ---------------------------------
                                # OR
                self.append(data)
                return
            elif current_node.data == key:
                # new_node = Node(data)
                nxt = current_node.next
                current_node.next = new_node
                new_node.next = nxt
                new_node.prev = current_node
                nxt.prev = new_node
            current_node = current_node.next


    def add_before_node(self, key, data):
        current_node = self.head

        while current_node:
            if current_node.prev is None and current_node.data == key:
                self.append(data)
                return
            elif current_node.data == key:
                new_node = Node(data)
                prev = current_node.prev
                prev.next = new_node
                current_node.prev = new_node
                new_node.next = current_node
                new_node.prev = prev
            current_node = current_node.next

#     DELETE
    def delete(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key and current_node ==self.head:
                # case-1
                if not current_node.next:
                    current_node = None
                    self.head = None
                    return
                # case-2
                else:
                    nxt = current_node.next
                    current_node.next = None
                    nxt.prev = None
                    current_node = None
                    self.head = nxt
                    return
            #     cas-3
            elif current_node.data ==key:
                if current_node.next:
                    nxt = current_node.next
                    prev = current_node.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current_node.next = None
                    current_node.prev = None
                    current_node = None
                    return
            # case-4
                else:
                    prev = current_node.prev
                    prev.next = None
                    current_node.prev = None
                    current_node = None
                    return
            current_node = current_node.next
#  REVERSE
    def reverse_node(self):
        temp = None
        cur = self.head

        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev

        if temp:
            self.head = temp.prev

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev
#     REMOVE DUPLICATES
    def remove_duplicate(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_for_removing_duplicates_node(cur)
                cur = nxt

    def delete_for_removing_duplicates_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                if cur.next is None:
                    cur = None
                    self.head = None
                else:
                    nxt = cur.next
                    cur.next = nxt
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur == node:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    prev.next =None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(4)
dllist.append(1)
dllist.append(2)
dllist.append(1)
dllist.append(5)




# dllist.prepend(9)
#
# dllist.add_after_node(1, 99)
# dllist.add_before_node(1, 111111)
# #
# dllist.print_dllist()
# dllist.delete(111111)
# print()
# dllist.print_dllist()

dllist.reverse()
# dllist.remove_duplicate()
dllist.print_dllist()


