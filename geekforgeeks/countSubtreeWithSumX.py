"""Given a binary tree containing N+1 nodes and an integer X. Your task is to complete the function countSubtreesWithSumX(), that returns the count of the number of subtress having total node’s data sum equal to a value X.
Example:

Input : 
Binary Tree:      5
                /   \  
             -10     3
             /  \   /  \
            9    8 -4   7
x = 7

Output : 2
1st one is leaf node:
7.

2nd one is:
      -10
     /   \
    9     8
Input:
The function takes a two argument as input, the reference pointer to the root of the binary tree and an integer denoting the value of X.
There will be T testcases and for each test case the function will be called separately.

Output:
For each test case the function should return the required answer.

Constraints:
1<=T<=103
1<=N<=103
-103 <=Node Value <= 103

Example:
Input:
2
6
5 -10 L 5 3 R -10 9 L -10 8 R 3 -4 L 3 7 R
7
2
1 2 L 1 3 R
5
Output:
2
0
"""

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def countSubtreesWithSumX(X, root):
    global count
    if root is None:
        return 0
    else:
        ls = countSubtreesWithSumX(X, root.left)
        rs = countSubtreesWithSumX(X, root.right)
    sums = ls + rs + root.value
    if sums == X:
        count+=1
    return sums    


        
#Binary Tree
x = Node(5)
x.left = Node(-10)
x.right = Node(3)

x.left.left = Node(9)
x.left.right = Node(8)

x.right.left = Node(-4)
x.right.right = Node(7)
#Binary Tree

count = 0
countSubtreesWithSumX(6, x)
print(count)
