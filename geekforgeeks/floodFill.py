"""Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace color of the given pixel and all adjacent(excluding diagonally adjacent) same colored pixels with the given color K.

Example:

                                {{1, 1, 1, 1, 1, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 0, 1, 1, 0, 1, 1},
                      {1, 2, 2, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 2, 2, 0},
                      {1, 1, 1, 1, 1, 2, 1, 1},
                      {1, 1, 1, 1, 1, 2, 2, 1},
                      };

                        x=4, y=4, color=3 

                               {{1, 1, 1, 1, 1, 1, 1, 1},
                     {1, 1, 1, 1, 1, 1, 0, 0},
                     {1, 0, 0, 1, 1, 0, 1, 1}, 
                     {1, 3, 3, 3, 3, 0, 1, 0},
                     {1, 1, 1, 3, 3, 0, 1, 0},
                     {1, 1, 1, 3, 3, 3, 3, 0},
                     {1, 1, 1, 1, 1, 3, 1, 1},
                     {1, 1, 1, 1, 1, 3, 3, 1}, };


Note: Use zero based indexing.


Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The first line of each test case contains Two integers N and M denoting the size of the matrix. Then in the next line are N*M space separated values of the matrix. Then in the next line are three values x, y and K.

Output:
For each test case print the space separated values of the new matrix.

Constraints:
1<=T<=100
1<=M[][]<=100

Example:
Input:
3
3 4
0 1 1 0 1 1 1 1 0 1 2 3
0 1 5
2 2
1 1 1 1
0 1 8
4 4 
1 2 3 4 1 2 3 4 1 2 3 4 1 3 2 4
0 2 9

Output:
0 5 5 0 5 5 5 5 0 5 2 3
8 8 8 8
1 2 9 4 1 2 9 4 1 2 9 4 1 3 2 4"""
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
    
    

t = int(input())
for tc in range(t):
    m, n = list(map(int, input().split(' ')))
    ip  = input()
    arr = [list(map(int, ip.strip().split(' ')))[n*start:n*start+n] for start in range(0, m)]
    x, y, k = list(map(int, input().split(' ')))
    visited = [[0 for v in range(n)] for z in range(m)]
    floodFill(arr, m, n, x, y, k, arr[x][y], visited)
    print(arr)
    
    