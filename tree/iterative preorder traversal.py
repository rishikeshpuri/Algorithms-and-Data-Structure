class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def iterativePreorder(root):
    if root is None:
        return
    nodeStack = []
    nodeStack.append(root)
    while len(nodeStack)>0:
        node = nodeStack.pop()
        print(node.data, end='-')

        if node.right is not None:
            nodeStack.append(node.right)

        if node.left is not None:
            nodeStack.append(node.left)

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
iterativePreorder(root)