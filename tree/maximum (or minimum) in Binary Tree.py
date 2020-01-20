# BY RECURSION

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_maximum(root):
    if root == None:
        return -99999999999
    current = root.data
    left_Current = find_maximum(root.left)
    right_current = find_maximum(root.right)

    if left_Current > current :
        current = left_Current

    if right_current > current:
        current = right_current

    return current

def find_minimum(root):
    if root == None:
        return 99999999999
    current = root.data
    left_Current = find_minimum(root.left)
    right_current = find_minimum(root.right)

    if left_Current < current :
        current = left_Current

    if right_current < current:
        current = right_current

    return current

tree = Node(-9)
tree.left = Node(1)
tree.right = Node(39)
tree.left.left = Node(9)
tree.left.right = Node(5)
tree.right.left =Node(6)
tree.right.right = Node(17)
# print('max element in tree is :', find_maximum(tree))
# print('min element in tree is :', find_minimum(tree))

# WHIT USING RECURSION

# ->BY LEVEL ORDER TRANSVERSAL

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def is_empty(self):
        return len(self.items) == []

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right =None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'max':
            return self.max_element(tree.root)
        if traversal_type == 'min':
            return self.min_element(tree.root)

    def max_element(self, start):
        if start == None:
            return

        queue = Queue()
        queue.enqueue(start)
        maxElement = 0
        traversal = ''
        while len(queue)>0:
            # traversal+= str(queue.peek()) + ''
            node = queue.dequeue()
            if maxElement < node.value:
                maxElement = node.value

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)
        return maxElement
    def min_element(self, start):
        if start == None:
            return

        queue = Queue()
        queue.enqueue(start)
        maxElement = 99999999
        # traversal = ''
        while len(queue)>0:
            # traversal+= str(queue.peek()) + ''
            node = queue.dequeue()
            if maxElement > node.value:
                maxElement = node.value

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)
        return maxElement
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left =Node(6)
tree.root.right.right = Node(7)
print('max element :',tree.print_tree('max'))
print('min element :',tree.print_tree('min'))
