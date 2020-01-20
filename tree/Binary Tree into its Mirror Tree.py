class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    # def preorder(self, start, traversal):
    #     if start:
    #         traversal += str(start.value) + "-"
    #         traversal = self.preorder(start.left,traversal)
    #         traversal = self.preorder(start.right, traversal)
    #     return traversal

    def mirror_By_Recursive(self, start):
        temp = start
        if start:
            self.mirror_By_Recursive(start.left)
            self.mirror_By_Recursive(start.right)

            start.left, start.right = start.right, start.left

            # temp = start.left
            # start.left = start.right
            # start.right = temp


        return start

    def levelOrderPrint(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal+= str(queue.peek())+ "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)
        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left =Node(6)
tree.root.right.right = Node(7)
# print(tree.preorder(tree.root, ''))

# tree.mirror_By_Recursive(tree.root)
# print('mirror of above ',tree.preorder(tree.root, ''))
print()
print('levelOrder', tree.levelOrderPrint(tree.root))
tree.mirror_By_Recursive(tree.root)
print('mirror ', tree.levelOrderPrint(tree.root))


