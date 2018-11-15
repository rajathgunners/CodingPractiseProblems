#AVL Insertion and Deletion - Self Balancing Tree
class node:
    
    def __init__(self, val):
        self.left = None
        self.value = val
        self.right = None
        self.height = 1
    #end class node

#SELF BALANCING FUNCTIONS OF AVL-TREE    
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



#FUNCTION TO INSERT INTO TREE
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



#FUNCTIONS TO DELETE FROM TREE
def rightMin(X):
    if X.left is None:
        return X.value
    else:
        return rightMin(X.left)
    

def avlDelete(root, val):
    if root is None:
        return root
    elif root.value is val:
        if root.left is None and root.right is None:
            return None
        elif root.right is None:
            return root.left
        elif root.left is None:
            return root.right
        else:
            root.value = rightMin(root.right)
            root.right = avlDelete(root.right, root.value)
    elif val > root.value:
        root.right = avlDelete(root.right, val)
    else:
        root.left = avlDelete(root.left, val)
    bal = balance(root.left, root.right)
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
X = avlInsert(X, 44) 
X = avlInsert(X, 35)
X = avlInsert(X, 50)
X = avlInsert(X, 40) 
X = avlInsert(X, 49)
X = avlInsert(X, 60)
X = avlInsert(X, 70) 

print(X.value)
print(X.left.value)
print(X.right.value)
print()
print(X.left.value)
print(X.left.right.value)
print()
print(X.right.value)
print(X.right.left.value)
print(X.right.right.value)
print()
print(X.right.right.value)
print(X.right.right.right.value)

X = avlDelete(X, 35)

print()
print()

print("After Deletion")
print(X.value)
print(X.left.value)
print(X.right.value)
print()
print(X.left.value)
print(X.left.left.value)
print(X.left.right.value)
print()
print(X.right.value)
print(X.right.right.value)