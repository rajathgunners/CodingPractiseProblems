#binary search tree Insertion, Inorder and Searching
 class node:
     def __init__(self, key):
          self.left = None
          self.right = None
          self.value = key
          #print("{} inserted".format(key))

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

def BSTSearch(X, skey):
     if X is None:
         return False
     elif skey is X.value:
         return True
     else:
         if skey > X.value:
             return BSTSearch(X.right, skey)
         else:
             return BSTSearch(X.left, skey)
     

        
 root = node(10)
 #BSTinsertion(root, 10)
 BSTinsertion(root, -5)
 BSTinsertion(root, 30)
 BSTinsertion(root,-10)
 BSTinsertion(root, 0)
 BSTinsertion(root, 5)
 BSTinsertion(root, 36)

#print(root.left.value)
 #print(root.left.right.value)
 BSTInorderTraversal(root)

sval = -50
 print()
 if BSTSearch(root, sval):
     print("{} is found".format(sval))
 else:
     print("{} is not found".format(sval))
