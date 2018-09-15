"""
            ________Dynamic Programming Beginner Problem_______________
Number of paths Submissions: 6371   Accuracy: 60.68%   Difficulty: Basic
Show Topic Tags         Amazon    Microsoft
The problem is to count all the possible paths from top left to bottom right of a  MxN matrix with the constraints that from each cell you can either move to right or down.

Input:
The first line of input contains an integer T, denoting the number of test cases.
The first line of each test case is M and N, M is number of rows and N is number of columns.

Output:
For each test case, print the number of paths.

Constraints:

1 ≤ T ≤ 30
1 ≤ M,N ≤ 10

Example:
Input
2
3 3
2 8
Output
6
8"""
def numberOfPaths(M, N):
    global arr
    if arr[M][N] > 0:
        return arr[M][N]
    else:
        arr[M][N] = numberOfPaths(M-1, N) + numberOfPaths(M, N-1)
        return arr[M][N]
        
        

    

arr = [[1 if i==0 or j==0 else 0 for i in range(10)] for j in range(10)]
t = int(input())
for tc in range(t):
    M, N = map(int, input().strip(' ').split(' '))
    print(numberOfPaths(M-1, N-1))