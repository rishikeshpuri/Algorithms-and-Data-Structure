class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_range(root, k1, k2):
    if root is None:
        return

    if k1 < root.value:
        print_range(root.left, k1,k2)

    if k1 <=root.value and k2 >= root.value:
        print(root.value, end=' ')

    if k2 > root.value:
        print_range(root.right, k1, k2)

k1= 10
k2 =25
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
print_range(root, k1, k2)
print()
print()
removeOutsideRange(root,k1,k2)