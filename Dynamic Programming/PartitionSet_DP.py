"""Given a set of numbers, check whether it can be partitioned into two subsets such that the sum of elements in both subsets is same or not.

Input:The first line contains an integer 'T' denoting the total number of test cases. Each test case constitutes of two lines. First line contains 'N', representing the number of elements in the set and the second line contains the elements of the set.
Output: Print YES if the given set can be partioned into two subsets such that the sum of elements in both subsets is equal, else print NO.
Constraints: 

1 <= T<= 100
1 <= N<= 100
0 <= arr[i]<= 1000

                   
Example:

Input:
2
4
1 5 11 5
3
1 3 5 

Output:

YES
NO"""
def subsetSum(arr, N, K):
    dp = [[0 for j in range(K+1)] for i in range(N+1)]
    
    for i in range(N+1):
        dp[i][0] = 1
    
    for j in range(1, K+1):
        dp[0][j] = 0
    
    for i in range(1, N+1):
        for j in range(1, K+1):
            dp[i][j] = dp[i-1][j]
            
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    
    return dp[N][K]
    

t = int(input())
for tc in range(t):
    N = int(input())
    arr = list(map(int, input().strip().split()))
    if sum(arr)%2==0:
        print(subsetSum(arr, N, sum(arr)//2))
    else:
        print(False)