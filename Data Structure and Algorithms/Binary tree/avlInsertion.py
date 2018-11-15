# AVL TREE INSERTION - SELF BALANCING TREE
class node:
    
    def __init__(self, val):
        self.left = None
        self.value = val
        self.right = None
        self.height = 1
    #end class node
    
def height(X):
    if X is None:
        return 0 
    else:
        return X.height
    
def balance(leftNode, rightNode):
    return (height(leftNode) - height(rightNode))

def setHeight(root):
    if root.right is None and root.left is None:
        return 1
    
    if root.right is None:
        return 1 + height(root.left)
    elif root.left is None:
        return 1 + height(root.right)
    else:
        return 1 + max(height(root.left), height(root.right))
    


def leftRotate(root):
    newRoot = root.right
    root.right = newRoot.left
    newRoot.left = root
    root.height = setHeight(root)
    newRoot.height = setHeight(newRoot)
    return newRoot
    
def rightRotate(root):
    newRoot = root.left
    root.left = newRoot.right
    newRoot.right = root
    root.height = setHeight(root)
    newRoot.height = setHeight(newRoot)
    return newRoot

def avlInsert(root, val):
    if root is None:
        return node(val)
    elif val >= root.value:
        root.right = avlInsert(root.right, val)
    else:
        root.left = avlInsert(root.left, val)
    bal = balance(root.left, root.right)
    
    #right case
    if bal < -1:
        # right-right case
        if height(root.right.right) > height(root.right.left):
            root = leftRotate(root)
        else:
            root.right = rightRotate(root.right)
            root = leftRotate(root)
    elif bal > 1:
        if height(root.left.left) > height(root.left.right):
            root = rightRotate(root)
        else:
            root.left = leftRotate(root.left)
            root = rightRotate(root)
    else:
        root.height = setHeight(root)
    return root



X = None
X = avlInsert(X, -10) 
X = avlInsert(X, 2)
X = avlInsert(X, 13)
X = avlInsert(X, -13) 
X = avlInsert(X, -15)
X = avlInsert(X, 15)
X = avlInsert(X, 17) 
X = avlInsert(X, 20)

print(X.value)
print(X.left.value)
print(X.right.value)
print()
print(X.left.value)
print(X.left.left.value)
print(X.left.right.value)
print()
print(X.right.value)
print(X.right.left.value)
print(X.right.right.value)
print()
print(X.right.right.value)
#print(X.right.right.left.value)
print(X.right.right.right.value)

"""
OUTPUT TO CHECK CORRRECTNESS
2
-13
15

-13
-15
-10

15
13
17

17
20
"""


  
	

 

  
	




