# To check if a path from Node-Leaf of B.T gives the required sum 
# Print out the path

class node:
    def __init__(self, key):
         self.left = None
         self.right = None
         self.value = key
         
         

def BTSum_LeaftoNode(X, sum):
    if X is None:
        return False
    if X.right is None and X.left is None:
        if X.value - sum is 0:
            return [X.value]
        else:
            return False
    else:
        r = BTSum_LeaftoNode(X.right, sum-X.value)
        l = BTSum_LeaftoNode(X.left, sum-X.value)
    if r and l:
        return [r + [X.value], l + [X.value]]
    elif r:
        return r + [X.value]
    elif l:
        return l + [X.value]
        



root1 = node(10)

root1.left = node(15)
root1.left.left = node(3)
root1.left.right = node(1)
root1.left.right.left = node(2)

root1.right = node(5)
root1.right.left= node(6)
root1.right.left.left= node(4)
root1.right.left.left.right= node(3)
root1.right.left.right= node(7)
root1.right.right = node(11)
root1.right.right.left = node(2)

l = BTSum_LeaftoNode(root1, 28)
if l is None:
    print("No path")
else:
    print(l)