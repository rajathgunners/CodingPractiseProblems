"""Given a N X N  matrix Matrix[N][N] of positive integers.  There are only three possible moves from a cell Matrix[r][c].

1. Matrix[r+1][c]

2. Matrix[r+1][c-1]

3. Matrix[r+1][c+1]

Starting from any column in row 0, return the largest sum of any of the paths up to row N-1.

Input:
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the order of matrix. Next line contains N*N integers denoting the elements of the matrix in row-major form.

Output:
Output the largest sum of any of the paths starting from any cell of row 0 to any cell of row N-1. Print the output of each test case in a new line.

Constraints:
1<=T<=20
2<=N<=20
1<=Matrix[i][j]<=1000 (for all 1<=i<=N && 1<=j<=N)

Example:

Input:
1
2
348 391 618 193

Output:
1009

Explanation: In the sample test case, the path leading to maximum possible sum is 391->618.  (391 + 618 = 1009)"""
def matrixPath(arr, N):
    dp = [[0 for j in range(N+2)] for i in range(N+1)]
    #print(type(dp))
    #print(type(arr))
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = arr[i-1][j-1] + max(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
    
    return max(dp[N])
            

t = int(input())
for tc in range(t):
    N = int(input())
    ip = map(int, input().strip().split())
    arr = [[next(ip) for j in range(N)] for i in range(N)]
    print(matrixPath(arr, N))
    