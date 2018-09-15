"""Given a Binary Tree find the length of the longest path which comprises of nodes with consecutive values in increasing order. Every node is considered as a path of length 1.longest-consecutive-sequence-in-Binary-tree-example
Input:

The first line of the input contains a single integer T denoting the number of test cases. For each test a root node is given to the longestConsecutive function. The only input to the function is the root of the binary Tree.
Output:

For each test case output in a single line, find the length of the longest path of the binary tree.
If no such sequence is possible return -1.

Constraints:

1<=T<=50
1<=N<=50
Example:

Input:

2
2
1 2 L 1 3 R
5
10 20 L 10 30 R 20 40 L 20 60 R 30 90 L

Output:

2
-1

Explanation:
Test case 1:

           1

        /     \

      2        3

For the above test case the longest sequence is : 1 2 

Test case 2:

            10

         /        \

     20          30

   /      \       /

40      60 90

For the above test case no sequence is possible: -1 """

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        return

def longestConsecutive(root):
    if root is None:
        return {'isseq': False, 'seql': 0, 'maxseq': 0}
    elif root.left is None and root.right is None:
        return {'isseq': True, 'seql': 1, 'maxseq': 1}
    else:
        l = longestConsecutive(root.left)
        r = longestConsecutive(root.right)
    
    if l['isseq'] and r['isseq']:
        if root.left.value - root.value == 1:
            #l['isseq'] = True
            l['seql'] += 1
        else:
            l['isseq'] = False
            l['seql'] = 1
        
        if root.right.value - root.value == 1:
            #r['isseq'] = True
            r['seql'] += 1
        else:
            r['isseq'] = False
            r['seql'] = 1
    
    elif l['isseq']:
        if root.left.value - root.value == 1:
            #l['isseq'] = True
            l['seql'] += 1
        else:
            l['isseq'] = False
            #l['seql'] = 1
    
    elif r['isseq']:
        if root.right.value - root.value == 1:
            #r['isseq'] = True
            r['seql'] += 1
        else:
            r['isseq'] = False
            #r['seql'] = 1
    #endif
    
    if l['isseq'] and r['isseq']:
        return {'isseq': True, 'seql': max(l['seql'],r['seql']), 'maxseq': max(l['seql'],r['seql'])}
    elif l['isseq']:
        return {'isseq': True, 'seql': l['seql'], 'maxseq': max(l['seql'], l['maxseq'], r['maxseq'])}
    elif r['isseq']:
        return {'isseq': True, 'seql': r['seql'], 'maxseq': max(l['maxseq'],r['seql'], r['maxseq'])}
    else:
         return {'isseq': True, 'seql': 1, 'maxseq': max(l['maxseq'],r['maxseq'])}
    #endif

    
    





#1 Test Case
x = Node(1)
x.left = Node(2)
x.left.left = Node(3)
x.left.left.left = Node(4)
x.left.left.right = Node(5)
x.left.left.left.left = Node(6)
x.left.left.left.left.right = Node(7)
x.left.left.left.left.right.left = Node(8)

print(longestConsecutive(x)['maxseq'])

#2 Test Case
x = Node(1)
x.right = Node(2)
x.right.right = Node(4)
x.right.right.right = Node(5)
x.right.right.right.right = Node(6)
x.right.right.right.right.right = Node(7)
x.right.right.right.right.right.left = Node(8)
print(longestConsecutive(x)['maxseq'])