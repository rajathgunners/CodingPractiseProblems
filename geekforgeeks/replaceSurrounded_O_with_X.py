"""Given a matrix of size NxM where every element is either ‘O’ or ‘X’, replace ‘O’ with ‘X’ if surrounded by ‘X’. A ‘O’ (or a set of ‘O’) is considered to be by surrounded by ‘X’ if there are ‘X’ at locations just below, just above, just left and just right of it.

Examples:

Input: mat[N][M] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                     {'X', 'O', 'X', 'X', 'O', 'X'},
                     {'X', 'X', 'X', 'O', 'O', 'X'},
                     {'O', 'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'O', 'X', 'O'},
                     {'O', 'O', 'X', 'O', 'O', 'O'},
                    };
Output: mat[N][M] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                      {'X', 'O', 'X', 'X', 'X', 'X'},
                      {'X', 'X', 'X', 'X', 'X', 'X'},
                      {'O', 'X', 'X', 'X', 'X', 'X'},
                      {'X', 'X', 'X', 'O', 'X', 'O'},
                      {'O', 'O', 'X', 'O', 'O', 'O'},
                    };

Input: mat[N][M] =  {{'X', 'X', 'X', 'X'}
                     {'X', 'O', 'X', 'X'}
                     {'X', 'O', 'O', 'X'}
                     {'X', 'O', 'X', 'X'}
                     {'X', 'X', 'O', 'O'}
                    };
Input: mat[N][M] =  {{'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'O', 'O'}
                    };

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The first line of each test case contains two integers N and M denoting the size of the matrix. Then in the next line are N*M space separated values of the matrix.

Output:
For each test case print the space separated values of the new matrix.

Constraints:
1<=T<=10
1<=mat[][]<=100
1<=n,m<=20

Example:
Input:
2
1 5
X O X O X 
3 3
X X X X O X X X X
Output:
X O X O X
X X X X X X X X X"""

def floodFill(arr, m, n, x, y, k, prev, visited):
    if (x < m and x > -1) and (y > -1 and y < n) :
        if visited[x][y] == 1:
            return
        else:
            visited[x][y] = 1
            if arr[x][y] == prev:
                arr[x][y] = k
                #print(arr)
                floodFill(arr, m, n, x, y-1, k, prev, visited)
                floodFill(arr, m, n, x, y+1, k, prev, visited)
                floodFill(arr, m, n, x-1, y, k, prev, visited)
                floodFill(arr, m, n, x+1, y, k, prev, visited)
            else:
                return
    else:
        return
    
def replace_O_with_hyphen(arr, N, M):
    for row in range(N):
        for col in range(M):
            if arr[row][col] == 'O':
                arr[row][col] = '-'

def replace_hyphen_with_O_boundary(arr, N, M):
    visited = [[0 for v in range(M)] for z in range(N)]
    for row in range(N):
        if row in [0, N-1]:
            m = list(range(M))
        else:
            m = [0, M-1]
        for col in m:
            floodFill(arr, N, M, row, col, 'O', '-', visited)
    
def replace_remaining_hyphen_with_X(arr, N, M):
    for row in range(N):
        for col in range(M):
            if arr[row][col] == '-':
                arr[row][col] = 'X'



def replaceSurrounded_O_with_X(arr, N, M):
    replace_O_with_hyphen(arr, N, M)
    #print(arr)
    replace_hyphen_with_O_boundary(arr, N, M)
    #print(arr)
    replace_remaining_hyphen_with_X(arr, N, M)
    #print(arr)
    

t = int(input())
for tc in range(t):
    n, m = list(map(int, input().split(' ')))
    ip  = input()
    arr = [list(ip.strip().split(' '))[n*start:n*start+n] for start in range(0, m)]
    #x, y, k = list(map(int, input().split(' ')))
    #visited = [[0 for v in range(n)] for z in range(m)]
    #floodFill(arr, m, n, x, y, k, arr[x][y], visited)
    replaceSurrounded_O_with_X(arr, n, m)
    for row in range(n):
        for col in range(m):
            print(arr[row][col], end = ' ')