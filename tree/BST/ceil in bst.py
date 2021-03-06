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

INT_MAX = -999999999

def ceil(root, key):
    if not root:
        return INT_MAX
    if root.data == key:
        return root.data

    if root.data < key:
        return ceil(root.right, key)
    ceilValue = ceil(root.left, key)
    return ceilValue if ceilValue >= key else root.data




tree = Node(7)
insert(tree, Node(10))
insert(tree, Node(5))
insert(tree, Node(3))
insert(tree, Node(6))
insert(tree, Node(8))
insert(tree, Node(12))
inOrder(tree)
print()
print(ceil(tree, 9))

