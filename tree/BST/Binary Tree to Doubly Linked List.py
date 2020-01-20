class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inOreder(root):
    if root:
        inOreder(root.left)
        print(root.value, end=' ')
        inOreder(root.right)

def fixPrevPtr(root):
    if root:
        fixPrevPtr(root.left)
        root.left = fixPrevPtr.pre
        fixPrevPtr.pre = root
        fixPrevPtr(root.right)

def fixNextPtr(root):
    prev = None
    while root and root.right:
        root = root.right

    while root and root.left:
        prev = root
        root = root.left
        root.right = prev
    return root

def BinaryTree_To_Dll(root):
    fixPrevPtr(root)
    return fixNextPtr(root)

def printList(root):
    while root:
        print(root.value, end=' ')
        root = root.right

root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

print("\n\t\t Inorder Tree Traversal\n")

inOreder(root)

fixPrevPtr.pre = None
head = BinaryTree_To_Dll(root)
print("\n\n\t\tDLL Traversal\n")
printList(head)
