"""Given a matrix with 0’s and 1’s , you enter the matrix at cell (0,0) in left to right direction. whenever you encounter a 0 you retain in same direction , if you encounter a 1’s you have to change direction to right of current direction and change that 1 value to 0, you have to find out from which index you will leave the matrix at the end.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines . The first line of each test case contains two integers n and m denoting the size of the matrix. Then in the next line are n*m space separated values of the matrix.

Output:
For each test case print in a new line two integers separated by space denoting the index of the matrix from which you will leave the matrix at the end.

Constraints:
1<=T<=100
1<=n,m<=20

Example:
Input:
2
3 3
0 0 1 0 0 0 0 0 0
2 4
0 0 0 1 0 0 1 1
Output:
2 2 
0 2"""


states = [[0, 1], [1, 0], [0, -1], [-1, 0]]
row, col = 0, 1

def exitPoint(arr, M, N):
    x, y = 0, 0
    st = 0
    while x >= 0 and x < M and y >= 0 and y < N:
        if arr[x][y] == 1:
            arr[x][y] = 0
            st = (st+1)%4
        
        x = x + states[st][row]
        y = y + states[st][col]
    
    print("{} {}".format(x - states[st][row], y-states[st][col]))
     

t = int(input())
for tc in range(t):
    M, N = map(int, input().split(' '))
    temp = [int(x) for x in input().split(' ')]
    arr = [temp[i*N:i*N+N] for i in range(M)]
    exitPoint(arr, M, N)
        