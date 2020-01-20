class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


count=0
def kthLargestlnBST(root, k):
    global count
    # count = 0
    if(not root):
        return None
    right= kthLargestlnBST(root.right, k)
    if( right ):
        return right
    count+= 1
    if(count == k):
        return root

    return kthLargestlnBST(root.left, k)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)
inorder(root)
print()
tree = kthLargestlnBST(root,4)
print(tree.data)
