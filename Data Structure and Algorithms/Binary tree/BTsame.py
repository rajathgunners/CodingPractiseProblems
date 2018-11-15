# check if 2 Binary Tree are same
class node:
    def __init__(self, key):
         self.left = None
         self.right = None
         self.value = key
         #print("{} inserted".format(key))


def BT_same(X1, X2):
    if X1 is None and X2 is None:
        return True
    elif X1 is None or X2 is None:
        return False
    else:
        return X1.value is X2.value and BT_same(X1.right, X2.right) and BT_same(X1.left, X2.left)
    
        

root1 = node(11)
root1.left = node(15)
root1.right = node(18)
root1.right.left = node(21)

root2 = node(11)
root2.left = node(15)
root2.right = node(18)
root2.right.left = node(21)

if BT_same(root1, root2):
    print("same")
else:
    print("not same")