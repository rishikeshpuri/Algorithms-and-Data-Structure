class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        currentNode = self.head
        if currentNode is None:
            print('No node')
            return
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.next
    def atBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = newNode

    def atMiddle(self,prev_node, data):
        if prev_node is None:
            print('no prev node')

        newNode = Node(data)
        newNode.next = prev_node.next
        prev_node.next = newNode
    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return
        prev1 = None
        current1 = self.head
        while current1 != None and current1.data != key1:
            prev1 = current1
            current1 = current1.next
        # print(prev1.data)
        # print(current1.data)

        prev2 = None
        current2 = self.head
        while current2 != None and current2.data != key2:
            prev2 = current2
            current2 = current2.next
        # print(prev2.data)
        # print(current2.data)

        if current1 == None or not current2:
            return

        if prev1:
            prev1.next = current2
        else:
            self.head = current2

        if prev2:
            prev2.next = current1
        else:
            self.head = current1

        current1.next, current2.next = current2.next, current1.next

    def len_iterative(self):
        count = 0
        current = self.head
        while current!=None:
            count+=1
            current = current.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1+ self.len_recursive(node.next)

    def delete_nodeWithDATA(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data!= key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

    def delete_node_at_position(self, pos):
        current_node = self.head

        if pos == 0:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        count = 0
        while current_node and count != pos:
            prev = current_node
            current_node = current_node.next
            count+=1
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None
#     REVERSE
    def reverse_iterative(self):
        prev = None
        current_node = self.head
        while current_node:
            nxt = current_node.next
            current_node.next = prev

            self.print_helper(prev, "PREV")
            self.print_helper(current_node, "CUR")
            self.print_helper(nxt, "NXT")
            print('\n')

            prev = current_node
            current_node = nxt
        self.head = prev
#     HELPER for reverse
    def print_helper(self, node, name):
        if node is None:
            print(name + ":None")
        else:
            print(name + ":" + node.data)

#     REVERSE BY RECURSIVE
    def reverse_recursive(self):
        def _reverse_recursive_(current_data, prev):
            if not current_data:
                return prev

            nxt = current_data.next
            current_data.next = prev
            prev = current_data
            current_data = nxt
            return _reverse_recursive_(current_data, prev)
        self.head = _reverse_recursive_(current_data=self.head, prev=None)

#     MERGE TWO SORT LINKED LIST
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data<=q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    def remove_duplicate(self):
        current = self.head
        prev = None

        dup_value = dict()

        while current:
            if current.data in dup_value:
#                 remove
                prev.next = current.next
                current = None
            else:
                dup_value[current.data] = 1
                prev = current
            current = prev.next

#     Nth to last node
    def print_nth_from_last(self, n):
#         method1
        total_length = self.len_iterative()
        current = self.head
        while current:
            if total_length == n:
                print(current.data)
                return current
            total_length -= 1
            current = current.next
        if current in None:
            return
#         method 2
#         p = self.head
#         q = self.head
#
#         count = 0
#         while q and count<n:
#             q = q.next
#             count+=1
#
#         if not q:
#             print(str(n) + "is greater than the number of node in the list")
#             return
#         while p and q:
#             p = p.next
#             q = q.next
#         return (p.data)

# COUNT OCCURENCE
#     method1
    def count_occurence_iterative(self, data):
        count = 0
        current = self.head
        while current:
            if current.data == data:
                count+=1
            current = current.next
        return count
    # method2
    def count_occurence_recursive(self, node, data):
        if node is None:
            return 0
        if node.data == data:
            return 1 + self.count_occurence_recursive(node.next, data)
        return self.count_occurence_recursive(node.next, data)
# ROTATE
    def rotate(self,k):
        p = self.head
        q = self.head
        count = 0
        prev = None

        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count+=1
        # print(prev.data)
        p = prev

        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

# PALINDROME

    def palindrome(self):
        s = ""
        p = self.head
        while p:
            s = s+ p.data
            p = p.next
        return s == s[::-1]

# MOVE TAIL TO HEAD
    def move_tail_to_head(self):
        last = self.head
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head
        second_to_last.next = None
        self.head = last
# SUM TWO LIST
    def sum_two_list(self, llist):
        p = self.head
        q = llist.head
        sum_list = LinkedList()
        carry = 0
        while p and q:
            if not p:
                i=0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i+j+carry
            print('s'+ ':'+ str(s))
            if s >=10:
                carry = 1
                remainder = s%10
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)

            if p:
                p = p.next

            if q:
                q = q.next

        sum_list.print()

sum_list1 = LinkedList()
sum_list2 = LinkedList()
sum_list1.append(5)
sum_list1.append(6)
sum_list1.append(3)

sum_list2.append(8)
sum_list2.append(4)
sum_list2.append(2)

sum_list1.print()
print()
sum_list2.print()
print(365+248)
sum_list1.sum_two_list(sum_list2)






# move_tail_to_head_llist = LinkedList()
# move_tail_to_head_llist.append('A')
# move_tail_to_head_llist.append('B')
# move_tail_to_head_llist.append('C')
# move_tail_to_head_llist.append('D')
# move_tail_to_head_llist.print()
# print()
# move_tail_to_head_llist.move_tail_to_head()
# move_tail_to_head_llist.print()


# palindrome_llist1 = LinkedList()
# palindrome_llist1.append('M')
# palindrome_llist1.append('A')
# palindrome_llist1.append('D')
# palindrome_llist1.append('A')
# palindrome_llist1.append('M')
#
# palindrome_llist2 = LinkedList()
# palindrome_llist2.append('A')
# palindrome_llist2.append('B')
# palindrome_llist2.append('C')
#
# palindrome_llist1.print()
# print()
# palindrome_llist2.print()
# print()
# print(palindrome_llist1.palindrome())
# print()
# print(palindrome_llist2.palindrome())


# rotate_llist = LinkedList()
# rotate_llist.append(1)
# rotate_llist.append(2)
# rotate_llist.append(3)
# rotate_llist.append(4)
# rotate_llist.append(5)
# rotate_llist.append(6)
# rotate_llist.print()
# print()
# rotate_llist.rotate(4)
# rotate_llist.print()



# count_llist = LinkedList()
# count_llist.append(1)
# count_llist.append(2)
# count_llist.append(1)
# count_llist.append(2)
# count_llist.append(3)
# count_llist.append(4)
# count_llist.print()
# print()
# print(count_llist.count_occurence_iterative(2))
# print(count_llist.count_occurence_recursive(count_llist.head, 2))

# nth_from_last = LinkedList()
# nth_from_last.append('A')
# nth_from_last.append('B')
# nth_from_last.append('C')
# nth_from_last.append('D')
# nth_from_last.print()
# print()
# print(nth_from_last.print_nth_from_last(2))



# llist_Duplicate = LinkedList()
# llist_Duplicate.append(1)
# llist_Duplicate.append(2)
# llist_Duplicate.append(3)
# llist_Duplicate.append(2)
# llist_Duplicate.append(1)
# llist_Duplicate.append(4)
# llist_Duplicate.append(5)
# llist_Duplicate.append(5)
# llist_Duplicate.append(5)
# llist_Duplicate.append(6)
# llist_Duplicate.print()
# print()
# llist_Duplicate.remove_duplicate()
# llist_Duplicate.print()

# -----MERGE TWO SHORT LIST----
# llist_1 = LinkedList()
# llist_2 = LinkedList()
#
# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)
#
# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)
#
# llist_1.print()
# print()
# llist_2.print()
# print()
# llist_1.merge_sorted(llist_2)
# llist_1.print()
# ---------END----------------







# llist = LinkedList()
# llist.atBeginning('A')
# llist.append('B')
# llist.append('C')
# llist.append('D')
# llist.atMiddle(llist.head, 'A')
# llist.print()
# print('---------------')
# llist.swap_nodes('B', 'C')
# llist.print()
# print('---------------')
# llist.swap_nodes('A', 'C')
# llist.print()
# print('Length of list by iteration', llist.len_iterative())
# print('Length of list by recursive', llist.len_recursive(llist.head))

# llist.delete_node_at_position(1)

# llist.reverse_recursive()
# llist.print()
