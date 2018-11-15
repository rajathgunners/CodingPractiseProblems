class node:
    def __init__(self, key):
         self.left = None
         self.right = None
         self.value = key
         #print("{} inserted".format(key))



def BT_Height(X):
    #lh, rh = 0, 0 
    if X is None:
        return 0
    else:
        lh = BT_Height(X.left)
        rh = BT_Height(X.right)
        return 1 + max(lh, rh)




root1 = node(11)
root1.left = node(15)
root1.right = node(18)
root1.right.left = node(21)


print(BT_Height(root1))