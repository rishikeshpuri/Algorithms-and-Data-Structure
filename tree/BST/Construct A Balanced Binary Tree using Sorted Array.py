class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def balanced_tree(arr, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    root = Node(mid)
    root.left = balanced_tree(arr, start, mid-1)
    root.right = balanced_tree(arr, mid+1, end)
    return root

def inorder(start):
    if start:
        inorder(start.left)
        print(start.value, end=' ')
        inorder(start.right)

arr = [1,2,3,4,5,6,7]
tree = balanced_tree(arr, 1, len(arr))
inorder(tree)