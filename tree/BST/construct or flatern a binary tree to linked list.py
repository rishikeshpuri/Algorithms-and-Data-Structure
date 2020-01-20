INT_MAX = 99999999


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#     def insert(self, data):


# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self):
#         if self.

def insert(root, data):
    if root is None:
        root = data
    else:
        if root.value > data.value:
            if root.left is None:
                root.left = data
            else:
                insert(root.left, data)

        elif root.value < data.value:

            if root.right is None:
                root.right = data
            else:
                insert(root.right, data)

def inOrder(start):
    if start:
        inOrder(start.left)
        print(start.value, end = ' ')
        inOrder(start.right)

tree = Node(50)
insert(tree, Node(30))
insert(tree, Node(20))
insert(tree, Node(40))
insert(tree, Node(70))
insert(tree, Node(60))
insert(tree, Node(80))
inOrder(tree)
