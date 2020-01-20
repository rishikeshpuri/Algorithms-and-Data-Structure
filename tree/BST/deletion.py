class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inOrder(self):
        if self:
            if self.left:
                self.left.inOrder()
            print(self.value)

            if self.right:
                self.right.inOrder()

    def _insert(self, data, cur_node):
        if data < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)

        elif data > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value is already present")

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def remove(self, data):
        # empty tree
        if self.root is None:
            return False

        # data is in root node
        elif self.root.value == data:
            if self.root.left is None and self.root.right is None:
                self.root = None

            elif self.root.left and self.root.right is None:
                self.root = self.root.left

            elif self.root.left is None and self.root.right:
                self.root = self.root.right

            elif self.root.left and self.root.right:
                delNodeParent = self.root
                delNode = self.root.right
                while delNode.left:
                    delNodeParent = delNode
                    delNode = delNode.left

                self.root.value = delNode.value
                if delNode.right:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.left = delNode.right
                    elif delNodeParent.value < delNode.value:
                        delNodeParent.right = delNode.right
                else:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.left = None
                    else:
                        delNodeParent.right = None
            return True

        parent = None
        node = self.root
        while node and node.value != data:
            parent = node
            if node.value > data:
                node = node.left
            elif node.value < data:
                node = node.right

        # case-1: data not found
        if node is None or node.value != data:
            return False
        # case-2: remove node have no children
        elif node.left is None and node.right is None:
            if data < parent.value:
                parent.left = None
            elif data > parent.value:
                parent.right = None
            return True
        # case-3: remove node have left child only
        elif node.left and node.right is None:
            if data < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left
            return True
        # case 4: remove-node has right child only
        elif node.left is None and node.right:
            if data < parent.value:
                parent.left = node.right
            else:
                parent.right = node.right
            return True
        # case 5: remove-node has left and right children
        else:
            delNodeParent = node
            delNode = node.right
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left

            node.value = delNode.value

            if delNode.right:
                if delNodeParent.value > delNode.value:
                    delNodeParent.left = delNode.right
                elif delNodeParent.value < delNode.value:
                    delNodeParent.right = delNode.right

            else:
                if delNodeParent.value > delNode.value:
                    delNodeParent.left = None
                else:
                    delNodeParent.right = None


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root._insert(data, self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def inOrder(self):
        if self.root:
            print("Inorder")
            self.root.inOrder()


tree = BinarySearchTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)
tree.inOrder()
print()
tree.remove(30)
tree.inOrder()
tree.remove(50)
tree.inOrder()
print(tree.find(30))
print(tree.find(80))