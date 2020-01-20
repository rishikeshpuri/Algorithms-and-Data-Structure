class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'inorder':
            return self.inOrder(deletion(tree.root, key), "")
        else:
            print("Traversal type" + str(traversal_type) + "not found")

    def inOrder(self, start, traversal):
        if start:
            traversal = self.inOrder(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self.inOrder(start.right, traversal)
        return traversal


def delete_deepest(root, d_node):
    queue = []
    queue.append(root)
    while len(queue)>0:
        node = queue.pop(0)
        if node is d_node:
            node = None
            return
        if node.right:
            if node.right is d_node:
                node.right = None
                return
            else:
                queue.append(node.right)
        if node.left:
            if node.left is d_node:
                node.left = None
                return
            else:
                queue.append(node.left)

def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    queue = []
    queue.append(root)
    while len(queue)>0:
        node = queue.pop(0)
        if node.value == key:
            key_node = node

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    if key_node:
        x = node.value
        delete_deepest(root, node)
        key_node.value = x
    return root




tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left =Node(6)
tree.root.right.right = Node(7)
key = 2
print("The tree before the deletion:")
print(tree.inOrder(tree.root, ''))
print("The tree after the deletion;")
print(tree.print_tree('preorder'))
