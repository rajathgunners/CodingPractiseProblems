""" Consider lines of slope -1 passing between nodes (dotted lines in below diagram). The diagonal sum in a binary tree is the sum of all node’s data lying between these lines. Given a Binary Tree, print all diagonal sums.

DiagonalSum

 
Image  ---> https://practice.geeksforgeeks.org/problems/diagonal-sum-in-binary-tree/1 
 

Input:
The first line consists of T test cases. The first line of every test case consists of N, denoting the number of edges in the tree. The second and third line of every test case consists of N, nodes of the binary tree.

Output:
Print space separated integers which are the diagonal sums for every diagonal present in the tree with slope -1.
 
Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
2
3
4 1 L 4 3 R 3 3 L
5
10 8 L 10 2 R 8 3 L 8 5 R 2 2 L

Output:
7 4 
12 15 3 """

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def diagonalSum(root, d):
    if root is None:
        return 0
    if d > 0:
        return diagonalSum(root.left, d-1) + diagonalSum(root.right, d)
    elif d == 0:
        return root.value + diagonalSum(root.right, d)


x = Node(1)
x.left = Node(2)
x.right = Node(3)

x.left.left = Node(9)
x.left.right = Node(6)

x.right.left = Node(4)
x.right.right = Node(5)

x.left.left.right = Node(10)
x.left.right.left = Node(11)

x.right.left.left = Node(12)
x.right.left.right = Node(7)

x.left.left.left = Node(100)
x.left.left.left.right = Node(101)

i = 0
while True:
    sums = diagonalSum(x, i)
    if sums == 0:
        break
    else:
        print("sums diagonal {} = {}".format(i+1, sums))
        i = i+1

    
    