# Input:  pre[] = {10, 30, 20, 5, 15},  preLN[] = {'N', 'N', 'L', 'L', 'L'}
# Output: Root of following tree
#           10
#          /  \
#         30   15
#        /  \
#       20   5

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructTree(preOreder, preLN, index_ptr, n):
    index = index_ptr[0]

    if index == n:
        return None

    node = Node(preOreder[index])
    index_ptr[0]+=1

    if preLN[index] == 'N':
        node.left = constructTree(preOreder, preLN, index_ptr, n)
        node.right = constructTree(preOreder, preLN, index_ptr, n)

    return node


def printInorder(node):
    if node == None:
        return
    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)

preOreder = [10, 30, 20, 5, 15]
preLN = ['N', 'N', 'L', 'L', 'L']
n = len(preOreder) 
index_ptr = [0]
root = constructTree(preOreder, preLN, index_ptr, n)

print("Following is Inorder Traversal of", "the Constructed Binary Tree:")
printInorder (root)