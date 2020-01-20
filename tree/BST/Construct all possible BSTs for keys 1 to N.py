class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    if (root != None):
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

def construct(start, end):
    list = []
    if start>end:
        list.append(None)
        return list
    for i in range(start, end+1):
        leftSubtree = construct(start, i-1)
        rightSubtree = construct(i+1, end)
        for j in range(len(leftSubtree)):
            left = leftSubtree[j]
            for k in range(len(rightSubtree)):
                right = rightSubtree[k]
                node = Node(i)
                node.left = left
                node.right = right
                list.append(node)

    return list


totalTreesFrom1toN = construct(1, 3)

print("Preorder traversals of all","constructed BSTs are")
for i in range(len(totalTreesFrom1toN)):
    preorder(totalTreesFrom1toN[i])
    print()
