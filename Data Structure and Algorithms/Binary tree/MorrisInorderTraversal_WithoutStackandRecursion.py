# Morris Inorder Traversal
# Inorder Traversal without stack and recursion

# moves CURRENT and right subtree to rightmost node of left child of CURRENT 

class node():
    
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None



def rightmostchild(Z, val):
    while Z.right is not None:
        if Z.right.value is val:
            Z.right = None
            return None
        Z = Z.right
        
    return Z    
        

def Morris(X):
    curr = X
    while curr is not None:
        if curr.left is None:
            print(curr.value, end = " ")
            curr = curr.right
        else:
            currpredecessor = rightmostchild(curr.left, curr.value)
            if currpredecessor is None:
                print(curr.value, end = " ")
                curr = curr.right
            else:
                currpredecessor.right = curr
                curr = curr.left
              

root = node(10)
root.left = node(5)
root.right = node(15)
root.left.left = node(2)
root.left.right = node(7)
root.right.right = node(30)

Morris(root)