class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inOrder(self):
        if self:
            if self.left:
                self.left.inOrder()
            print(self.value, end='-')

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


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root._insert(data, self.root)

    def inOrder(self):
        if self.root:
            print("Inorder")
            self.root.inOrder()

    def is_bst_satisfied(self):
        if self.root:
            is_satisfied = self._is_bst_satisfied(self.root, self.root.value)

            if is_satisfied is None:
                return True
            return False
        return True
    def _is_bst_satisfied(self, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.value:
                return self._is_bst_satisfied(cur_node.left, cur_node.left.value)
            else:
                return False

        if cur_node.right:
            if data < cur_node.right.value:
                return self._is_bst_satisfied(cur_node.right, cur_node.right.value)
            else:
                return False


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

bst = BinarySearchTree()
bst.root = Node(1)
bst.root.left = Node(2)
bst.root.right = Node(3)
print(tree.is_bst_satisfied())
print(bst.is_bst_satisfied())