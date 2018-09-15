
#0/1 Knapsack problem D.P

def knapsack(wt, val, dp, N, W):

       

    for i in range(N+1):

        for j in range(W+1):

            if i==0 or j==0:

                dp[i][j] = 0

            else:
                
                if wt[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]], dp[i-1][j])

    #print(dp)

    return dp[N][W]

def find_weights(dp, wt, N, W):
    i = N
    j = W
    wts = []
    while j > 0:
        if dp[i][j] == dp[i-1][j]:
            i=i-1
        else:
            
            wts.append(wt[i-1])
            j = j - wt[i-1]
            i = i - 1
    return wts        
        

 

t = int(input())

for tc in range(t):

    N = int(input())

    W = int(input())

    val = list(map(int, input().strip().split()))

    wt  = list(map(int, input().strip().split()))

    dp = [[-1 for j in range(0,W+1)] for i in range(N+1)]

    #print(dp)

    print(knapsack(wt, val, dp, N, W))
    print(find_weights(dp, wt, N, W))