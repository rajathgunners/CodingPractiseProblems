#total number of unique BST
"""Given an integer N, how many structurally unique binary search trees are there that store values 1...N?

For example, for N = 2, there are 2 unique BSTs
     1               2  
      \            /
       2         1
For N = 3, there are 5 possible BSTs
  1              3        3         2      1
    \           /        /           /    \      \
     3        2         1        1    3      2
    /       /                \                      \
   2      1               2                        3

Input:
First line contains the test cases T.  1<=T<=15
Each test case have one line which is an interger N.  1<=N<=11

Example:
Input:
2
2
3

Output:
2
5"""






countarr = [2 if i == 2 else 5 if i == 3 else 1 if i==1 or i==0 else 0 for i in range(12)]

def uniqueBST(N):
    global countarr
    if countarr[N] != 0:
        return countarr[N]
    else:
        tot = 0
        for i in range(1, N+1):
            l = i-1
            r = N-i
            tot += (uniqueBST(l) * uniqueBST(r))
        
        countarr[N] = tot
    return tot

t = int(input())
for tc in range(t):
    N = int(input())
    print(uniqueBST(N))