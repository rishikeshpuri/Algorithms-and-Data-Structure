# BY RECURSION
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(root):
    if root == None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height+1, right_height+1)

def rightToLeft(root, level):
    if root == None:
        return 0
    if level ==1:
        print(root.value, end=' ')
    elif level>1:
        rightToLeft(root.right, level-1)
        rightToLeft(root.left, level-1)

def leftToRight(root, level):
    if root == None:
        return 0
    if level ==1:
        print(root.value, end=' ')

    elif level>1:
        leftToRight(root.left, level-1)
        leftToRight(root.right, level-1)

def reverseSpiral(root):
    flag = 1
    h = height(root)
    for i in range(h, 0, -1):
        if flag == 1:
            leftToRight(root, i)

            flag=0
        elif flag == 0:
            rightToLeft(root, i)

            flag =1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
reverseSpiral(root)