class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca(root, n1, n2):
    if root is None:
        return None

    if (root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)

    if (root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)

    return root.data
# OR
def lca_by_iterative(root, n1,n2):
    while root:
        if root is None:
            return None
        if (root.data > n1 and root.data > n2):
            root = root.left
        if (root.data < n1 and root.data < n2):
            root = root.right
        else:
            break
    return root.data



root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
n1 = 8
n2 = 22

print(lca(root, n1, n2))
print('lca_by_iterative :', lca_by_iterative(root, n1, n2))