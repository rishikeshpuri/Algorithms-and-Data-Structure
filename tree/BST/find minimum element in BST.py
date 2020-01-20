class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def finding_minimun_Element(self,root):
        if root is None:
            return root

        currentNode = root
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode.value
#     by recursion
    def findMin(self, root):
        currentNode = root
        if currentNode.left == None:
            return currentNode.value
        else:
            return self.findMin(currentNode.left)

tree = BinarySearchTree(10)
tree.root.left = Node(6)
tree.root.right = Node(16)
tree.root.left.left = Node(4)
tree.root.left.right = Node(9)
tree.root.right.left = Node(13)
tree.root.left.right.left = Node(7)

print(tree.finding_minimun_Element(tree.root))
print(tree.findMin(tree.root))


