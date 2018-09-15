
"""Given a preorder traversal of a BST, print the leaf nodes of the tree without building the tree.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the no of nodes of the BST. Then in the next line are N space separated values denoting the preorder traversal of the binary tree.

Output:
For each test case in a new line print the leaf nodes separated by space of the BST in sorted order.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
2
5
890 325 290 530 965 
3
3 2 4

Output:
290 530 965
2 4 """


def printLeafNodesFromPreOrder(pre):
    stack = list()
    i, j = 0, 1
    while j < len(pre):
        if pre[i] > pre[j]:
            stack.append(pre[i])
        else:
            leaf = False
            while stack:
                if pre[j] > stack[-1]:
                    stack.pop()
                    leaf=True
                else:
                    break
            if leaf:
                print(pre[i], end=' ')
        #print(stack)
        i=i+1
        j=j+1
    print(pre[i], end = ' ')
    

t = int(input())
for tc in range(t):
    n = int(input())
    s = (input().split(' '))
    if '' in s:
        s.remove('')
    pre = list(map(int, s))
    
    printLeafNodesFromPreOrder(pre)
    print()