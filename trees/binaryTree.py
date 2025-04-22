class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTreeNodes():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')


root = buildTreeNodes()

print("InOrder traversal:")
inOrder(root)
print("")


print("PreOrder traversal:")
preOrder(root)
print("")



print("PostOrder traversal:")
postOrder(root)
print("")





