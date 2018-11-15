# FINDING LEAST COMMON ANCESTOR

class node():
    
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def LCA(X, val1, val2):
    if X is None:
        return False
    L = LCA(X.left, val1, val2)
    R = LCA(X.right, val1, val2)
    T = X.value is val1 or X.value is val2
    if L and R or L and T or R and T:
        print(X.value)
    else:
        return L or R or T
        
root = node(10)
root.left = node(-10)
root.right = node(30)
root.left.right = node(8)
root.right.left = node(25)
root.right.right = node(60)
root.right.right.left = node(28)
root.right.right.right = node(78)

LCA(root, 28, 78)
    