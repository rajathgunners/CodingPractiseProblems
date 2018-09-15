"""Write a function to print spiral order traversal of a tree. For below tree, function should print 1, 2, 3, 4, 5, 6, 7.
        1
      /   \
    2      3
   / \    / \
  7  6   5   4

Input:
The task is to complete the method which takes one argument, root of the Tree. The struct node has a data part which stores the data, pointer to left child and pointer to right child.
There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should print level order traversal in spiral form .

Constraints:
1 <=T<= 30
1 <=Number of nodes<= 3000
1 <=Data of a node<= 1000

Example:
Input:
2
2
1 2 R 1 3 L
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
1 3 2
10 20 30 60 40

There are two test casess.  First case represents a tree with 3 nodes and 2 edges where root is 1, left child of 1 is 3 and right child of 1 is 2.   Second test case represents a tree with 4 edges and 5 nodes."""

def heightBinarytree(root):
    if root is None:
        return 0
    else:
        return 1 + max(heightBinarytree(root.left), heightBinarytree(root.right))

def isEven(ht):
    if ht%2==0:
        return True
    else:
        return False

def printSpiralLevelOrderUtil(root, ht, iseven):
    if ht == 0:
        print(root.value, end=" ")
    else:
        if iseven:
            printSpiralLevelOrderUtil(root.right, ht-1, iseven)
            printSpiralLevelOrderUtil(root.left, ht-1, iseven)
        else:
            printSpiralLevelOrderUtil(root.left, ht-1, iseven)
            printSpiralLevelOrderUtil(root.right, ht-1, iseven)
    
    


def printSpiralLevelOrder(root):
    ht = heightBinarytree(root)
    for h in range(ht):
        printSpiralLevelOrderUtil(root, h, isEven(h))

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        return
#BinaryTree example
x = Node(1)
x.left = Node(2)
x.right = Node(3)
x.left.left = Node(7)
x.left.right = Node(6)
x.right.left = Node(5)
x.right.right = Node(4)

#calling function
printSpiralLevelOrder(x)