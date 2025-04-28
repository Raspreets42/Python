from collections import deque

class BinarySearchTree:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
        
    def height(self):
        if self is None:
            return -1
        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1
        return max(left_height, right_height) + 1
        
    def diameter(self):
        # If want diameter in edges,then,
        # left_height +right_height (not +1)
        
        # If want diameter in nodes, then,
        # left_height + right_height + 1
        
        self.max_diameter = 0
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)

            # Update diameter at this node
            self.max_diameter = max(self.max_diameter, left_height + right_height + 1)
            return 1 + max(left_height, right_height)
        height(self)
        return self.max_diameter

        
    def insert(self,value):
        if value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
                
    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.data, end=' ')
        if self.right:
            self.right.inOrder()
    
    def preOrder(self):
        print(self.data,end=' ')
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.data,end=' ')
        
    def searchNode(self,value):
        if self.data == value:
            return "Found"
        if value < self.data and self.left:
            return self.left.searchNode(value)
        if value > self.data and self.right:
            return self.right.searchNode(value)
        return "Not Found"
        
    def deleteNode(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.deleteNode(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.deleteNode(value)
        else:
            # Node to delete is found
            # Case 1 and 2: Node with only one child or no child
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # Case 3: Node with two children
            # Find inorder successor (smallest in the right subtree)
            min_larger_node = self.right.findMinNode()
            self.data = min_larger_node.data
            # Delete the inorder successor
            self.right = self.right.deleteNode(min_larger_node.data)
        return self

    def findMinNode(self):
        current = self
        while current.left:
            current = current.left
        return current
        
    # New Breadth-First Traversal method
    def levelOrder(self):
        queue = deque()
        queue.append(self)
        
        while queue:
            node = queue.popleft()
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    # Find Minimum
    def findMin(self):
        current = self
        while current.left:
            current = current.left
        return current.data

    # Find Maximum
    def findMax(self):
        current = self
        while current.right:
            current = current.right
        return current.data
        
    # Lowest Common Ancestor (LCA)
    def lowestCommonAncestor(self, n1, n2):
        if self is None:
            return None
        if n1 < self.data and n2 < self.data:
            return self.left.lowestCommonAncestor(n1, n2)
        if n1 > self.data and n2 > self.data:
            return self.right.lowestCommonAncestor(n1, n2)
        return self.data
        
            
arr = [8,4,9,2,7,3,5,1,6]
bst = BinarySearchTree(arr[0])

for e in arr[1::]:
    bst.insert(e)
    
print("\nIn-Order : ",end='')
bst.inOrder()
print("\nPre-Order : ",end='')
bst.preOrder()
print("\nPost-Order : ",end='')
bst.postOrder()
print("\nLevel-Order : ", end='')
bst.levelOrder()

print("\n\nSearching 0: ", end=' ')
print(bst.searchNode(0))

print("Searching 4: ", end=' ')
print(bst.searchNode(4))

print("Searching 10: ", end=' ')
print(bst.searchNode(10))

# Deleting a node
print("\nDeleting node 4...")
bst = bst.deleteNode(4)
print("In-Order after deleting 4 : ", end='')
bst.inOrder()

print("\n\nFindMin : ",bst.findMin(),end='')
print("\nFindMax : ",bst.findMax(),end='')
print("\n\nHeight of the Tree : ",bst.height(),end='')
print("\nDiameter of the Tree : ",bst.diameter(),end='')
print("\n\nlowestCommonAncestor of 2,7: ",bst.lowestCommonAncestor(2,7))
print("lowestCommonAncestor of 2,9: ",bst.lowestCommonAncestor(2,9))

