class binaryTreeNode:
    def __init__(self, value, left, right):
        self.value = value 
        self.left = left 
        self.right = right

    def __init__(self, value):
        self.value = value

    def setLeftChild(self, node):
        self.left = node 

    def setRightChild(self, node):
        self.right = node