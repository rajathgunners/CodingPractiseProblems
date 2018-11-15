#Finding Largest BST in a binary tree in O(n)

#Pre order  -> NLR  -> top to bottom
#Post order -> LRN  -> bottom to top
# return {'isbst': XXX, 'size': XXX, 'min': XXX, 'max': XXX}
class node():
    
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def longestbst(X):
    if X is None:
        return {'isbst':True, 'size':0, 'min':0, 'max':0}
    
    elif X.left is None and X.right is None:
        return {'isbst':True, 'size':1, 'min':X.value, 'max':X.value}
    
    else:
        L = longestbst(X.left)
        R = longestbst(X.right)
        
        if L['isbst'] and R['isbst'] and X.value > L['max'] and X.value < R['min']:
            return {'isbst': True, 'size': 1+L['size']+R['size'], 'min': L['max'], 'max':R['min']}
        
        else:
            return {'isbst': False, 'size': max(L['size'], R['size']), 'min': 0, 'max': 0}
        

root = node(25)

root.left = node(18)
root.left.left = node(19)
root.left.right = node(20)
root.left.left.right = node(15)
root.left.right.left = node(18)
root.left.right.right = node(25)

root.right = node(20)
root.right.left = node(35)
root.right.right = node(60)
root.right.left.left = node(20)
root.right.left.right = node(40)
root.right.left.left.right = node(50)

root.right.right.left = node(55)
root.right.right.right = node(70)

print(longestbst(root)['size'])
        