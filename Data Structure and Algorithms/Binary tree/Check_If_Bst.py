class node:
    def __init__(self, key):
         self.left = None
         self.right = None
         self.value = key
         #print("{} inserted".format(key))


# my method with time complexity > O(n)
"""def Check_If_Bst(X):
    if X is None:
        return []
    
    elif X.right is None and X.left is None:
        return [X.value]
    
    else:
        r = Check_If_Bst(X.right)
        l = Check_If_Bst(X.left)
        
        if not ( r or l ):
            return []
        
        else:
            if l:
                for il in l:
                    if il > X.value:
                        return []
            
            if r:
                for ir in r:
                    if ir < X.value:
                        return []
        return r + l + [X.value]"""


#better method with time complexity O(n)
def Check_If_Bst(X, low = -1000, high = 1000 ):
    if X is None:
        return True
    else:
        return X.value > low and X.value < high and Check_If_Bst(X.left, low, X.value) and Check_If_Bst(X.right, X.value, high)
    
        
            
        




root1 = node(10)

root1.left = node(7)
root1.left.left = node(-20)
root1.left.right = node(8)

root1.right = node(25)
root1.right.left = node(16)
root1.right.right = node(32)


if Check_If_Bst(root1):
    print ("BST")
else:
    print("Not BST")

