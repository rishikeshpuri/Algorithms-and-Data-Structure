class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.value, end='-')

            if self.right:
                self.right.inorder()

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

        elif self.value < data:
            if self.right:
                return self.right.find(data)
            else:
                return False



class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inorder_predecessor(self, data):
        store = 0
        if self.root is None:
            return None
        while True:
            if self.root.value > data:
                self.root = self.root.left
            elif self.root.value < data:
                store = self.root.value
                self.root = self.root.right

            else:
                if self.root.left:
                    temp = self.root.left
                    while temp.right:
                        temp = temp.right
                    return temp.value

                elif self.root.left is None:
                    while self.root.value != data:
                        if self.root.value < data:
                            store = self.root.value
                            self.root = self.root.right
                        elif self.root.value > data:
                            self.root = self.root.left
                    return store




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
        if self:
            self.root.inorder()


# Let us create following BST
#                 50
#                /  \
#               /    \
#             30     70
#            / \     / \
#           /   \   /   \
#          20   40 60   80

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
# print(tree.find(40))
print(tree.inorder_predecessor(30))
