#Longest Increasing Subsequence

def LIS(arr, dp, N):
    for i in range(N):
        for j in range(i-1, -1, -1):
            if (arr[i] > arr[j]) and (dp[i] <= dp[j]):
                dp[i] = dp[j]+1
    
    return max(dp)


t = int(input())
for tc in range(t):
    N = int(input())
    arr = list(map(int, input().strip().split()))
    dp = [1 for i in range(N)]
    if N == 0:
        print(0)
    else:
        print(LIS(arr, dp, N))