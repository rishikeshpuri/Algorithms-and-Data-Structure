class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    queue = []
    stack = []
    queue.append(root)
    while len(queue)>0:
        root = queue.pop(0)
        stack.append(root)

        if root.right:
            queue.append(root.right)

        if root.left:
            queue.append(root.left)


    while len(stack)>0:
        root = stack.pop()
        print (root.value, end=' ')

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
print("Level Order traversal of binary tree is")
reverseLevelOrder(tree)