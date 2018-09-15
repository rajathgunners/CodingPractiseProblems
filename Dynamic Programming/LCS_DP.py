#Longest Common Subsequence using Dynamic Programming

def LCS(dp, text1, text2, n1, n2):
    for i in range(n1+1):
        for j in range(n2+1):
            #print("[{}][{}]".format(i, j))
            if i==0 or j==0:
                dp[i][j] = 0
            elif text1[i-1]==text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return(dp[n1][n2])


t = int(input())
for tc in range(t):
    s1 = input("enter s1")
    s2 = input("enter s2")
    n1 = len(s1)
    n2 = len(s2)
    dp = [[-1 for j in range(n2+1)] for i in range(n1+1)]
    #print(dp)
    print(LCS(dp, s1, s2, n1, n2))
    #print(dp)