"""Given an integer N denoting the Length of a line segment. you need to cut the line segment in such a way that the cut length of a line segment each time is integer either x , y or z. and after performing all cutting operation the total number of cutted segments must be maximum. 


Input
first line of input contains of an integer 'T' denoting number of test cases
first line of each testcase contains N .
second line of each testcase contains 3 space separated integers x , y and z.

Output
For each test case print in a new line an integer corresponding to the answer .


Constraints
1<=t<=70
1<=N,x,y,z<=4000


Example

Input

2
4
2 1 1
5
5 3 2


Output
4
2"""
def CuttingRod(N, x, y, z):
    dp = [-4000 for i in range(N+1)]
    
    dp[0] = 0
    
    mins = min(x, y, z)
    #print("mins = {}".format(mins))
    if mins == 1:
        return N
    
    for i in range(1, mins):
        dp[i] = -4000
    
    for j in range(mins, N+1):
        if x>j:
            _x = -4000
        else:
            _x = dp[j-x]
        
        if y>j:
            _y = -4000
        else:
            _y = dp[j-y]
        
        if z>j:
            _z = -4000
        else:
            _z = dp[j-z]
        
        dp[j] = 1 + max(_x, _y, _z)
        
    
    #print(dp)
    return dp[N]
    

t = int(input())
for tc in range(t):
    N = int(input())
    x, y, z = list(map(int, input().strip().split()))
    print(CuttingRod(N, x, y, z))
