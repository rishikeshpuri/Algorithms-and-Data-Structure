class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, currentNode):
    if root is None:
        root = currentNode
    else:
        if root.data > currentNode.data:
            if root.left is None:
                root.left = currentNode
            else:
                insert(root.left, currentNode)
        else:
            if root.right is None:
                root.right = currentNode
            else:
                insert(root.right, currentNode)

def inOrder(start):
    if start:
        inOrder(start.left)
        print(start.data, end = ' ')
        inOrder(start.right)

tree = Node(50)
insert(tree, Node(30))
insert(tree, Node(20))
insert(tree, Node(40))
insert(tree, Node(70))
insert(tree, Node(60))
insert(tree, Node(80))
inOrder(tree)

# --------------- ITERATIVE METHOD--------------------
# def insert_iteratively(root, currentNode):
#     newNode = Node(currentNode)
#     x = root
#     y = None
#     while x:
#         y = x
#         if currentNode < x.data:
#             x = x.left
#         else:
#             x = x.right
#     if y == None:
#         y = newNode
#     elif currentNode < y.data:
#         y.left = newNode
#     else:
#         y.right = newNode
#     return y
#
# def inOrder(start):
#     if start:
#         inOrder(start.left)
#         print(start.data, end = ' ')
#         inOrder(start.right)
#
# root = None
# root = insert_iteratively(root, 50)
# insert_iteratively(root, 30)
# insert_iteratively(root, 20)
# insert_iteratively(root, 40)
# insert_iteratively(root, 70)
# insert_iteratively(root, 60)
# insert_iteratively(root, 80)
# inOrder(root)
