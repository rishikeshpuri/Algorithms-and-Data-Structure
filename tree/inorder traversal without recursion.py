class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderIterative(root):
    if not root:
        return

    current = root
    stk = []

    while True:
        if current is not None:
            stk.append(current)
            current = current.left

        elif stk:
            current = stk.pop()
            print(current.data, end='-')
            current = current.right
        else:
            break
    # print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inOrderIterative(root)