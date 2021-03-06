"""Frog steps either 1, 2 or 3 steps to go to top. In how many ways it reaches the top?

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N. Where is the number of steps it has to hop.

Output:

Print the number of ways.

Constraints:

1 ≤ T ≤ 50
1 ≤ N ≤ 50

Example:

Input:
2
1
5

Output:
1
13"""

def tot_steps(dist):
    dp = [ 1 if i==0 else 0 for i in range(dist+1) ]
    for i in range(1, dist+1):
        if i==1:
            dp[i] = 1
        elif i==2:
            dp[i] = 2
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[dist]

t = int(input())
for tc in range(t):
    N = int(input())
    print(tot_steps(N))