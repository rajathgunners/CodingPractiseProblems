#BST DELETION - #3 CASES
class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        #print("{} inserted".format(key))
#--------------------------
def leftMinValue(X):
    if X.left is None:
        return X.value
    else:
        return leftMinValue(X.left)
        
def BSTDeletion(X, val):
    if X is None:
        print("Element Not Found, Cannot Be Deleted")
        return X
    if X.value is val:
        #leaf node
        if X.right is None and X.left is None:
            return None
        
        #node with single child
        elif X.left is None:
            return X.right
        elif X.right is None:
            return X.left
        
        #node with 2 children
        else:
            X.value = leftMinValue(X.right)
            X.right = BSTDeletion(X.right, X.value)
    elif val > X.value:
        X.right = BSTDeletion(X.right, val)
    else:
        X.left = BSTDeletion(X.left, val)
    return X
#----------------------------------------------



def BSTinsertion(X,val):
    if val >= X.value:
        if (X.right == None):
            X.right = node(val)
        else:
            BSTinsertion(X.right,val)
    else:
        if (X.left == None):
            X.left = node(val)
        else:
            BSTinsertion(X.left,val)


def BSTInorderTraversal(X):
    if X is None:
        return
    else:
        BSTInorderTraversal(X.left)
        print(X.value, end = "\t")
        BSTInorderTraversal(X.right)
        return


    
        
    
     


root = node(5)
BSTinsertion(root, 2)
BSTinsertion(root, 12)
BSTinsertion(root,-4)
BSTinsertion(root, 3)
BSTinsertion(root, 9)
BSTinsertion(root, 21)
BSTinsertion(root, 19)
BSTinsertion(root, 25)

BSTInorderTraversal(root)

print()

root = BSTDeletion(root, 2)# Deletion process
    

BSTInorderTraversal(root)