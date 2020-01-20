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
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'maxlevelsum':
            return self.max_level_sum(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def max_level_sum(self, start):
        if start is None:
            return
        
        result = start.value
        queue = Queue()
        queue.enqueue(start)
        
        while len(queue) > 0:
            count = queue.size()
            sum = 0
            while count:
                node = queue.dequeue()
                sum+= node.value

                if node.left:
                    queue.enqueue(node.left)
    
                if node.right:
                    queue.enqueue(node.right)
                count -= 1 
            result = max(sum, result)
            print('sum at this level', result)
        return result

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(8)
tree.root.right.right.left =Node(6)
tree.root.right.right.right = Node(7)

print(tree.print_tree('maxlevelsum'))