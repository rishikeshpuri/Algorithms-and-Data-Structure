# Input: inorder[] = {5, 10, 40, 30, 28}
# Output: root of following tree
#          40
#        /   \
#       10     30
#      /         \
#     5          28
#
# Input: inorder[] = {1, 5, 10, 40, 30,
#                     15, 28, 20}
# Output: root of following tree
#           40
#         /   \
#        10     30
#       /         \
#      5          28
#     /          /  \
#    1         15    20

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(inOrder, start, end):
    if start > end:
        return None

    i = max_value(inOrder, start, end)

    node = Node(inOrder[i])

    if start == end:
        return node

    node.left = buildTree(inOrder,start,i-1)
    node.right = buildTree(inOrder, i+1, end)

    return node

def max_value(arr, start, end):
    i = 0
    max_value = arr[start]
    maxindex = start
    for i in range(start+1, end+1):
        if arr[i]> max_value:
            max_value = arr[i]
            maxindex = i
    return maxindex


def printInorder(node):
    if node == None:
        return
    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)

inorder = [5, 10, 40, 30, 28]
end = len(inorder) - 1
root = buildTree(inorder, 0, end)
print("Inorder traversal of the",  "constructed tree is ")
printInorder(root)