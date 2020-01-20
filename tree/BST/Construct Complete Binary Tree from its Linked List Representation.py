class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Conversion:
    def __init__(self):
        self.head =None
        self.root = None

    def push_at_beginning(self, new_data):
        newNode = ListNode(new_data)
        newNode.next = self.head
        self.head = newNode

    def convertList_to_BinaryTree(self):
        q= []
        if self.head is None:
            self.root = None
            return
        self.root = BinaryTree(self.head.data)
        q.append(self.root)
        self.head = self.head.next
        while self.head:
            parent = q.pop(0)

            leftChild = None
            rightChild = None
            leftChild = BinaryTree(self.head.data)
            q.append(leftChild)
            self.head = self.head.next

            if self.head:
                rightChild = BinaryTree(self.head.data)
                q.append(rightChild)
                self.head = self.head.next

            parent.left = leftChild
            parent.right = rightChild

    def inorderTraversal(self, root):
        if (root):
            self.inorderTraversal(root.left)
            print(root.data, end= ' ')
            self.inorderTraversal(root.right)

conv = Conversion()
conv.push_at_beginning(36)
conv.push_at_beginning(30)
conv.push_at_beginning(25)
conv.push_at_beginning(15)
conv.push_at_beginning(12)
conv.push_at_beginning(10)
conv.convertList_to_BinaryTree()
print("Inorder Traversal of the contructed Binary Tree is:")
conv.inorderTraversal(conv.root)