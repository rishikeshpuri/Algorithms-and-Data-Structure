class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def delete_binaryTree(root):
    if root ==None:
        return 0
    delete_binaryTree(root.left)
    delete_binaryTree(root.right)
    print(root.value, end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print('deleting it ')
delete_binaryTree(root)
print()
root = None
print('tree deleted')