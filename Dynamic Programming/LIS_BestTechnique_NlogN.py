#Important coding challenges
#Longest Increasing Subsequence in O(nlogn) Time complexity

from bisect import bisect_left

def LIS(arr, N):
    dp = [0 for _ in range(N)]
    lens = 0
    
    for a in arr:
        i = bisect_left(dp, a, 0, lens)
        dp[i] = a
        
        if i==lens:
            lens += 1
    
    return lens


N = int(input())

arr = list(map(int, input().strip().split()))

print(LIS(arr, N))
     
        
