class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def findingElement(self,root, key):
        if not root:
            return None

        currentNode = root
        while currentNode and key != currentNode.value:
            if key > currentNode.value:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
        return currentNode

tree = BinarySearchTree(7)
tree.root.left = Node(4)
tree.root.right = Node(9)
tree.root.left.left = Node(2)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(10)

print(tree.findingElement(tree.root, 9))