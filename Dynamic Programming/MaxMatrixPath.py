"""Given a n*n matrix where all numbers are distinct, find the maximum length path (starting from any cell) such that all cells along the path are in increasing order with a difference of 1.

We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1) with the condition that the adjacent cells have a difference of 1.

Example:

Input:  mat[][] = {{1, 2, 9}
                   {5, 3, 8}
                   {4, 6, 7}}
Output: 4
The longest path is 6-7-8-9. """

def PrintMat(mat):
    for i in range(len(mat)):
        print(mat[i])

    return


def FindLongestPath(arr, dp, i, j, R, C):
    if dp[i][j] != -1:
        return dp[i][j]
    
    if (i<0 or i>=R) or (j<0 or j>=C):
        return 0
    
    if j<C-1 and arr[i][j+1] == arr[i][j]+1:
        dp[i][j] = 1 + FindLongestPath(arr, dp, i, j+1, R, C)
        
        
    elif  j>0 and arr[i][j-1] == arr[i][j]+1:
        dp[i][j] = 1 + FindLongestPath(arr, dp, i, j-1, R, C)
    
    elif i<R-1 and arr[i+1][j] == arr[i][j]+1:
        dp[i][j] = 1 + FindLongestPath(arr, dp, i+1, j, R, C)
    
    elif i>0 and arr[i-1][j] == arr[i][j]+1:
        dp[i][j] = 1 + FindLongestPath(arr, dp, i-1, j, R, C)
    
    else:
        dp[i][j] = 1
    
    return dp[i][j]
        
        
def LongestPath(arr, R, C):
    longest_path = 0
    dp = [[-1 for j in range(C)] for i in range(R)]
    
    for i in range(R):
        for j in range(C):
            result = FindLongestPath(arr, dp, i, j, R, C)
            dp[i][j] = max(dp[i][j], result)
            if longest_path < dp[i][j]:
                longest_path = dp[i][j]
    
    return longest_path
    #PrintMat(dp)
    


t = int(input())
for tc in range(t):
    R = int(input())
    C = int(input())
    arr = map(int, input().strip().split())
    mat = [[next(arr) for j in range(C)] for i in range(R)]
    print(LongestPath(mat, R, C))
