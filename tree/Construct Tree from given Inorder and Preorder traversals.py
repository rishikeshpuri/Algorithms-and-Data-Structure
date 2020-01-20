class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(inOrder, preOrder, inStart, inEnd):
    if inStart > inEnd:
        return None
    tNode = Node(preOrder[buildTree.preOrderIndex])
    buildTree.preOrderIndex += 1
    inOrderIndex = search(inOrder, inStart, inEnd, tNode.data)

    tNode.left = buildTree(inOrder, preOrder, inStart, inOrderIndex -1)
    tNode.right = buildTree(inOrder, preOrder, inOrderIndex +1, inEnd)

    return tNode

def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i

def print_inOrder(start):
    if start:
        print_inOrder(start.left)
        print(start.data, end='-')
        print_inOrder(start.right)

inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
buildTree.preOrderIndex = 0
inStart=0
inEnd = len(inOrder)-1
root = buildTree(inOrder, preOrder, inStart, inEnd)
print_inOrder(root)
