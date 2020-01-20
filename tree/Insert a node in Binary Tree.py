class Node:
    def __init__(self, value):
        self.value =value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preOrder(self, start, traversal):
        if start:
            traversal+= str(start.value) +'-'
            traversal = self.preOrder(start.left, traversal)
            traversal = self.preOrder(start.right, traversal)
        return traversal

    def print_tree(self):
        return self.preOrder(insert(tree.root, 77), '')

class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == []

    def enqueue(self, item):
        self.items.insert(0, item)

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

def insert(root, key):
    newNode = Node(key)
    if root is None:
        root = newNode
        return root
    queue = Queue()
    queue.enqueue(root)
    while len(queue)>0:
        node = queue.dequeue()
        # print(node.value)
        if node.left:
            queue.enqueue(node.left)
        else:
            node.left = newNode
            return root
        if node.right:
            queue.enqueue(node.right)
        else:
            node.right = newNode
            return root

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
# tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left =Node(6)
tree.root.right.right = Node(7)
print("original tree before insertion :", tree.preOrder(tree.root,''))
print("original tree After insertion :", tree.print_tree())
# print(insert(tree.root, 33))