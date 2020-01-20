# Root to leaf path sum equal to a given number

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def hasPathSum(node, sum):
    if node is None:
        return sum == 0

    subSum = sum - node.data
    ans = 0

    if subSum == 0 and node.left == None and node.right == None:
        return True
    if node.left:
        ans = ans or hasPathSum(node.left, subSum)

    if node.right:
        ans = ans or hasPathSum(node.right, subSum)

    return ans

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.right.left = Node(2)
sum = 21
if hasPathSum(root, sum):
    print("There is a root-to-leaf path with sum",sum)
else:
    print("There is no root-to-leaf path with sum ",sum)