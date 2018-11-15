#SUM OF NODES OF BINARY TREE

class node:
     
     def __init__(self, key):
         self.left = None
         self.right = None
         self.value = key


 root = node(1)
 root.left = node(2)
 root.right = node(3)
 root.left.left = node(4)
 root.left.right = node(5)
 root.left.left.left = node(6)
 root.left.left.right = node(7)
 root.right.left = node(8)
 root.right.right = node(9)
 root.right.left.right = node(10)

def BinaryTreeSumNodes(X):
     if X is None:
         return 0
     else:
         return X.value + BinaryTreeSumNodes(X.left) + BinaryTreeSumNodes(X.right)

print(BinaryTreeSumNodes(root))
